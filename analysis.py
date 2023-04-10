import numpy as np
import matplotlib.pyplot as plt

# dir = "data/With_learning_reward/"
dir = "./"
print(f'{dir}coords.npy')
coords = np.load(f'{dir}coords.npy')
dopamine = np.load(f'{dir}dopamine.npy')
vta_gaba = np.load(f'{dir}vta_gaba.npy')
insulin = np.load(f'{dir}insulim.npy')
ach = np.load(f'{dir}ach.npy')
r_tan = np.load(f'{dir}tan.npy')
hunger = np.load(f'{dir}hunger.npy')
satiety = np.load(f'{dir}satiety.npy')
approach = np.load(f'{dir}approach.npy')
avoid = np.load(f'{dir}avoid.npy')


figure, ax = plt.subplots(4, 1)

i1 = 0
i2 = len(dopamine)
ax[0].plot(insulin[i1:i2], label = "Gherlin")

# ax[0].plot(ach, label = "Ach")
# ax[0].plot(r_tan, label = "Tan")
# ax[0].plot(dopamine, label = "Dopamine")
ax[0].legend()

ax[1].plot(hunger[i1:i2], label = "Hunger")
ax[1].plot(satiety[i1:i2], label = "Satiety")
ax[1].legend()

ax[2].plot(approach[i1:i2], label = "Approach")
ax[2].plot(avoid[i1:i2], label = "Avoid")
ax[2].legend()

ax[3].plot(dopamine[i1:i2], label = "Dopamine")
ax[3].plot(vta_gaba[i1:i2], label = "VTA_gaba")
ax[3].legend()
ax[3].set_xlabel('Time step')
plt.show()
