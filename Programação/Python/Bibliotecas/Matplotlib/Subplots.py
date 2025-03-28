import matplotlib.pyplot as plt
import numpy as np

xa_array = np.linspace(0, 3, 50)
ya_array = np.exp(xa_array)

fig,(ax1, ax2) = plt.subplots(2,2)

ax1[0].plot(xa_array, ya_array, 'g')
ax2[0].plot(xa_array, ya_array, 'r--')
ax1[1].plot(xa_array, ya_array, 'y+')
ax2[1].plot(xa_array, ya_array)

plt.show()