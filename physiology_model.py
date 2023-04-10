import numpy as np

class Physiology:
    def __init__(self):
        self.insulin = 0.0
        self.leptin = 1.0

    def f(self, reward):
        d_insulin = 0.08*(1 - self.insulin) - reward*self.insulin
        d_leptin = 0

        return d_insulin, d_leptin

    def step( self, h, reward ):
        d_insulin, d_leptin = self.f(reward)
        self.insulin += h*d_insulin
        self.leptin = np.heaviside(0.5-self.insulin, 0)

        return self.insulin, self.leptin