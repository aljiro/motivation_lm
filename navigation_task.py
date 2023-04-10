from motivation_model import Motivation
from physiology_model import Physiology
from ach_model import Ach
# from navigation_model_sham import *
from navigation_model import *
import numpy as np
import matplotlib.pyplot as plt
import rospy

class NavigationTask:
    def __init__( self, T ):
        self.T = T
        self.Xtan = np.zeros( T )
        self.Xapproach = np.zeros( T )
        self.Xavoid = np.zeros( T )
        self.Xhunger = np.zeros( T )
        self.Xsatiety = np.zeros( T )
        self.Xach = np.zeros( T )
        self.Xd = np.zeros( T )
        self.Xvta_gaba = np.zeros( T )
        self.Xinsulin = np.zeros( T )
        self.Xcoords = np.zeros((2,T))
        self.time = np.zeros( T )
        self.h = 0.01
        self.tau_elig = 1.0
        self.eta = 0.01
        self.robo_replay = NavigationModel(self.tau_elig, self.eta)

    def run( self ):
        
        motivation = Motivation()
        physiology = Physiology()
        ach_model = Ach()
        
        reward = 0

        for i in range(self.T):
            insulin, leptin = physiology.step( self.h, reward*2 )
            d, vta_gaba, hunger, satiety, approach, avoid = motivation.step( self.h, insulin, leptin, reward )
            r_tan = ach_model.step( self.h, vta_gaba, d )
            ach = np.heaviside(r_tan-0.4, 0)

            # print("Ach: ", ach, ", rtan: ", r_tan, ", i: ", i)

            if i > 1000:
                reward, coords = self.robo_replay.step(d, ach)
                self.Xapproach[i] = approach
                self.Xavoid[i] = avoid
                self.Xsatiety[i] = satiety
                self.Xhunger[i] = hunger
                self.Xtan[i] = r_tan
                self.Xach[i] = ach
                self.Xd[i] = d
                self.Xvta_gaba[i] = vta_gaba
                self.Xinsulin[i] = insulin
                self.Xcoords[:, i] = coords

            if rospy.core.is_shutdown():
                break

        print("Saving data")
        np.save("dopamine.npy", self.Xd)
        np.save("vta_gaba.npy", self.Xvta_gaba)
        np.save("insulim.npy", self.Xinsulin)
        np.save("ach.npy", self.Xach)
        np.save("tan.npy", self.Xtan)
        np.save("hunger.npy", self.Xhunger)
        np.save("approach.npy", self.Xapproach)
        np.save("avoid.npy", self.Xavoid)
        np.save("satiety.npy", self.Xsatiety)
        np.save("coords.npy", self.Xcoords)
        
        # plt.figure()
        # plt.plot(self.Xd)
        # plt.plot(self.Xinsulin)
        # plt.plot(self.Xach)

        # plt.figure()
        # plt.plot(self.Xcoords[0,:], self.Xcoords[1, :])
        # plt.show()

if __name__ == '__main__':
    nav_task = NavigationTask(300000)
    nav_task.run()




