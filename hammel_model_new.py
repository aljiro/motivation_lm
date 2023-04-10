import numpy as np
class Hammel:
    
    def __init__(self):
        # Receptors
        self.h = 0.08
        sigma = 0.1
        self.tau = 2.0
        self.response_w = lambda T: 1.0/(1 + np.exp(-0.1*(T - 35.0)))
        self.response_c = lambda T: 1.0/(1 + np.exp(0.1*(T - 30.0)))
        # Activation
        self.g = lambda x: x*(x > 0.0)
        # State
        self.X = np.array([0, 0, 1, 0, 0])
        self.t = 0.0

    def f( self, t, x, T):
        w_warm = w_cold = w_sp_sen = w_sen_w = w_ins_w = w_sen_c = w_ins_c = 2.0
        sp = x[0]
        sen = x[1]
        ins = x[2]
        w = x[3]
        c = x[4]

        d_sp = lambda x: (-(x - 0) + self.g( w_warm*self.response_w(T) - w_cold*self.response_c(T)))/self.tau
        d_sen = lambda x: (-x + self.g( w_sp_sen*sp))/self.tau
        d_ins = lambda x: 0
        d_w = lambda x: (-x + self.g( w_sen_w*sen - w_ins_w*ins))/self.tau
        d_c = lambda x: (-x + self.g( -w_sen_c*sen + w_ins_c*ins))/self.tau

        return np.array([d_sp(sp), d_sen(sen), d_ins(ins), d_w(w), d_c(c)])

    def step( self, temperature ):
        self.X = self.X + self.h*self.f(self.t, self.X, temperature)
        self.t = self.t + self.h

        return self.X[3], self.X[4]