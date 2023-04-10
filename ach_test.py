import numpy as np
import matplotlib.pyplot as plt
from ach_model import *

T = 20000
h = 0.01
ach = Ach()
Xrtan = np.zeros(T)
Xmsn = np.zeros(T)
Xgaba = np.load("vta_gaba.npy")
Xda = np.load("dopamine.npy")
Xgaba = Xgaba[:T]
Xda = Xda[:T]

for i in range(T):

    r_tan = ach.step(h, Xgaba[i], Xda[i])
    Xrtan[i] = r_tan
    Xmsn[i] = ach.r_msn

fig, ax = plt.subplots(1, 1)
ax.plot(Xrtan, linewidth = 2.0, label = "CIN")
# ax[0].plot(Xmsn)

ax.plot(Xda, label = "DA", linewidth = 2.0)
# ax[1].plot(Xgaba, label = "GABA")
ax.legend()
ax.set_xlabel('time_step')

plt.show()