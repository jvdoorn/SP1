"""
Graph for problem 120 of SP1.
"""

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 20, 1000)
y = np.square(x) * np.exp(x) / (1 + np.exp(x))**2

plt.style.use(['science', 'grid'])
plt.plot(x, y)
plt.title('Schottky heat capacity')
plt.xlabel('$\\frac{\\epsilon}{k_BT}$')
plt.ylabel('$\\frac{C_V}{Nk_B}$')
plt.savefig('export/problem120.svg')
plt.show()
