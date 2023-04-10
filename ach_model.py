import numpy as np

class Ach:
    def __init__(self):
        self.r_tan = 1
        self.r_msn = 0

    def f( self, r_vta_gaba, r_vta_da ):
        # Both increase
        # w_msn_tan = -2.5;
        # w_gaba_msn = -1.9
        # w_tan = 1.5

        # beta = 5;
        # f = lambda u: 1./(1 + np.exp(-beta*u));
        # d_msn = -self.r_msn + f( w_gaba_msn*r_vta_gaba + 0.1 );
        # d_tan = -self.r_tan + f( w_tan*r_vta_da + w_msn_tan*self.r_msn - 0.5 );

        # Increase + Dip
        w_msn_tan = 3.5;
        w_gaba_msn = -1.0
        w_tan = -1.4
        w = -1.5

        beta1 = 10;
        f1 = lambda u: 1./(1 + np.exp(-beta1*u));
        beta2 = 2;
        f2 = lambda u: 1./(1 + np.exp(-beta2*u));
        d_msn = -self.r_msn + f2( w_gaba_msn*r_vta_gaba + 0.1 );
        d_tan = -self.r_tan + f1( w_tan*r_vta_da + w_msn_tan*self.r_msn - 0.6 );

        # w_msn_tan = -4.1;
        # w_gaba_msn = -3.9
        # w_tan = 3.0

        # beta1 = 10;
        # f1 = lambda u: 1./(1 + np.exp(-beta1*u));
        # beta2 = 2;
        # f2 = lambda u: 1./(1 + np.exp(-beta2*u));
        # d_msn = -self.r_msn + f1( w_gaba_msn*r_vta_gaba + 0.1 );
        # d_tan = -self.r_tan + f2( w_tan*r_vta_da + w_msn_tan*self.r_msn + 0.1);

        return d_tan, d_msn

    def step( self, h, r_vta_gaba, r_vta_da):
        d_tan, d_msn = self.f(r_vta_gaba, r_vta_da)
        self.r_tan += h*d_tan
        self.r_msn += h*d_msn
        

        return self.r_tan