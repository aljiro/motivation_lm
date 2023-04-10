import numpy as np
class Motivation:
    def __init__(self):
        N = 10
        self.r = np.zeros(N)
        self.r[1] = 1.9

    def hammel_model( self, r, we, wi, insulin ):
        # Parameters
        # Time constants
        tau_sen = 1;
        tau_ins = 1;
        tau_h = 1;
        tau_s = .5;

        # Rates
        k_ins = 0; # Constant, mostly

        # Weights
        w_energy = 0.5;
        w_sen_h = we;
        w_ins_h = -wi;
        w_sen_s = -wi;
        w_ins_s = we;

        # External input

        # Rate function
        beta = 8;
        f = lambda u: 1./(1 + np.exp(-beta*u));
        g = lambda u: beta*u;

        # Previous values
        r_sen = r[0];
        r_ins = r[1];
        r_h = r[2];
        r_s = r[3];

        # Map
        dr_sen = -r_sen/tau_sen + g( w_energy*insulin )/tau_sen;
        dr_ins = k_ins/tau_ins;
        dr_h = -r_h/tau_h + f( w_sen_h*r_sen + w_ins_h*r_ins )/tau_h;
        dr_s = -r_s/tau_s + f( w_sen_s*r_sen + w_ins_s*r_ins )/tau_s;

        dr = np.array([dr_sen,
            dr_ins,
            dr_h,
            dr_s])
        return dr

    def acc_model( self, r, w, theta ):        
        beta = 1;
        f = lambda u: 1./(1 + np.exp(-beta*u));
        dr = -r + f(w*r - theta);

        return dr

    def f( self, r, insulin, leptin, reward ):
        # Parameters
        W_h = 10;
        s_h = 0.47;
        w_hammel = s_h*W_h;
        q_hammel = (1-s_h)*W_h;
        w_acc = 8.3;

        # Weights
        w_acc_app = -0.6; # NAcc -> Approach: Inhibition
        w_h_app = 0.6; # Hunger -> approach : excitation
        w_avoid_app = 0; # Avoid -> approach : 
        w_s_avoid = 0.6; # Satiety -> avoid : excitation
        w_app_avoid = 0; # Approach -> avoid : 
        w_app_vta = -0.5; # Approach -> vta_gaba: inhibition
        w_avoid_vta = 0.5; # Avoid -> vta_gaba: excitation
        w_gaba_da = -0.6; # vta_gaba -> vta_da: inhibition
        w_orexin_da = 0.5; # Orexin -> vta_da: excitatory
        w_leptin_orexin = -0.5; # Leptin -> orexin: excition with more leptin
        w_reward = 0.9;

        # Currents
        # Rate function
        beta = 8;
        f = lambda u: 1./(1 + np.exp(-beta*u));

        beta = 40;
        g = lambda u: 1./(1 + np.exp(-beta*u));
        # f = @(u)beta*u;

        # Previous values
        # Hammel rates
        r_hammel = r[0:4];

        r_sen = r[0];
        r_ins = r[1];
        r_hunger = r[2];
        r_satiety = r[3];

        r_approach = r[4];
        r_avoid = r[5];
        r_vta_gaba = r[6];
        r_vta_da = r[7];
        r_orexin = r[8];
        r_acc_d1 = r[9];

        # Map
        dr_hammel = self.hammel_model( r_hammel, w_hammel, q_hammel, insulin );
        dr_approach = -r_approach + f( w_acc_app*r_acc_d1 + w_h_app*r_hunger + w_avoid_app*r_avoid);
        dr_avoid = -r_avoid + f( w_s_avoid*r_satiety + w_app_avoid*r_approach ); # BNST connection missing
        dr_vta_gaba = -r_vta_gaba + f( w_app_vta*r_approach + w_avoid_vta*r_avoid  );
        dr_vta_da = -r_vta_da + g( w_gaba_da*r_vta_gaba + w_orexin_da*r_orexin );
        dr_orexin = -r_orexin + f( w_leptin_orexin*leptin + 0.5 );

        # Accumbal subsystem
        theta = (r_vta_da - 0.2)*10;
        dr_acc_d1 = self.acc_model( r_acc_d1, w_acc, theta ) + w_reward*reward

        dr = np.concatenate((dr_hammel,np.array([
            dr_approach,
            dr_avoid,
            dr_vta_gaba,
            dr_vta_da,
            dr_orexin,
            dr_acc_d1])))

        return dr

    def step( self, h, insulin, leptin, reward ):
        self.r = self.r + h*self.f(self.r, insulin, leptin, reward)
        dop = self.r[7]
        vta_gaba = self.r[6]
        hunger = self.r[2]
        satiety = self.r[3]
        approach = self.r[4]
        avoid = self.r[5]
        return dop, vta_gaba, hunger, satiety, approach, avoid
