import numpy as np
import matplotlib.pyplot as plt

dir = "./"
# dir = "data/With_learning_reward/"
coords = np.load(f'{dir}coords.npy')
dopamine = np.load(f'{dir}dopamine.npy')
insulin = np.load(f'{dir}insulim.npy')
ach = np.load(f'{dir}ach.npy')
rtan = np.load(f'{dir}tan.npy')

k = 1200
coords = coords[:, k:]
dopamines = dopamine[k:]
rtan = rtan[k:]


hend = np.heaviside(rtan - 0.4, 0)
hini = np.heaviside(0.2 - rtan, 0)

figure, ax = plt.subplots(2, 1)

ax[0].plot(dopamine, linewidth = 2.0, label = "Dopamine")
ax[0].plot(insulin, linewidth = 2.0,  label = "insulin")
ax[0].plot(ach, linewidth = 2.0,  label = "Ach")
ax[0].legend()
ax[0].set_xlabel('Iteration')
ax[0].set_title('Physiological variables')

ax[1].plot(hend)
ax[1].plot(hini)

figure, ax = plt.subplots(1, 2)

ini_idx = np.diff(hini)
ini_idx = np.where(ini_idx < 0)[0]
end_idx = np.diff(hend)
end_idx = np.where(end_idx > 0)[0]

N = min(len(ini_idx), len(end_idx))

for i in range(N):
    idx0 = ini_idx[i]
    idx1 = end_idx[i]
    ax[0].plot( coords[0, idx0:idx1], coords[1, idx0:idx1], 'r', alpha = i/N )
    ax[0].plot( coords[0, idx0], coords[1, idx0], 'r.', markersize = 10 )
    ax[0].plot( coords[0, idx1], coords[1, idx1], 'rD', markersize = 8 )
    ax[0].plot(0, 0.7, 'ko', markersize = 10)
    ax[0].plot(0, 0.7, 'r+', markersize = 8)
    ax[0].axis([-1, 1, -1, 1])
    # plt.pause(1)
    # ax[0].cla()
ax[0].set_xlabel('X')
ax[0].set_ylabel('Y')
ax[0].set_title('Hungry trajectories')

for i in range(N):
    idx1 = ini_idx[i+1]
    idx0 = end_idx[i] 
    ax[1].plot( coords[0, idx0:idx1], coords[1, idx0:idx1], 'k', alpha = i/N )
    ax[1].plot( coords[0, idx0], coords[1, idx0], 'k.', markersize = 10 )
    ax[1].plot( coords[0, idx1], coords[1, idx1], 'kD', markersize = 8 )
    ax[1].plot(0, 0.7, 'ro', markersize = 10)
    ax[1].plot(0, 0.7, 'k+', markersize = 8)
    ax[1].axis([-1, 1, -1, 1])

# ax[1].plot(coords[0, :], coords[1, :], 'k', linewidth = 1.0)

# ax[1].plot(coords[0, dopamines > 0.5], coords[1,dopamines > 0.5], 'r', linewidth = 2.0)
# ax[1].plot(coords[0, dopamines <= 0.5], coords[1, dopamines <= 0.5], 'k', linewidth = 1.0)

# ax[1].plot(0, 0.7, 'r.', markersize = 10)
ax[1].set_xlabel('X')
ax[1].set_ylabel('Y')
ax[1].set_title('Satiated trajectories')


plt.show()
