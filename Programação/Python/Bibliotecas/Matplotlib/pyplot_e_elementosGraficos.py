import matplotlib.pyplot as plt
import numpy as np

xa_array = np.linspace(0, 2*np.pi, 500)
ya_array = np.sin(xa_array)

xb_array = np.linspace(0, 2*np.pi, 500)
yb_array = np.sin(xa_array + np.pi/2)

plt.plot(xa_array,ya_array, 'k--', label = 'func a')
plt.plot(xb_array,yb_array, 'r-', label = 'func b')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()

