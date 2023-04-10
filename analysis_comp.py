import numpy as np
import matplotlib.pyplot as plt

coords_ach = np.load('coords_withach.npy')
dopamine_ach = np.load('dopamine_withach.npy')
insulin_ach = np.load('insulim_withach.npy')
ach_ach = np.load('ach_withach.npy')

coords_no_ach = np.load('coords_noach.npy')
dopamine_no_ach = np.load('dopamine_noach.npy')
insulin_no_ach = np.load('insulim_noach.npy')
ach_no_ach = np.load('ach_noach.npy')

figure, ax = plt.subplots(1, 2)

ax[0].plot(dopamine_ach)
ax[0].plot(insulin_ach)
ax[0].plot(ach_ach)

ax[1].plot(coords_ach[0,:], coords_ach[1,:], linewidth = 2.0)

figure, ax = plt.subplots(1, 2)

ax[0].plot(dopamine_no_ach, linewidth = 2.0, label = "Dopamine")
ax[0].plot(insulin_no_ach, linewidth = 2.0,  label = "insulin")
ax[0].plot(ach_no_ach, linewidth = 2.0,  label = "Ach")
ax[0].legend()
ax[0].set_xlabel('Iteration')
ax[0].set_title('Physiological variables')
ax[1].plot(coords_no_ach[0,ach_no_ach==1], coords_no_ach[1,ach_no_ach==1], 'r', linewidth = 2.0)
ax[1].plot(coords_no_ach[0,ach_no_ach==0], coords_no_ach[1,ach_no_ach==0], 'k', linewidth = 2.0)
ax[1].plot(0, 0.7, 'r.', markersize = 10)
ax[1].set_xlabel('X')
ax[1].set_ylabel('Y')
ax[1].set_title('MiRo\'s position')

plt.show()
