"""
Simulation for problem 09 of SP1.
"""
import math

import matplotlib.pyplot as plt
import numpy as np

g = 9.8  # Gravitational constant
r = 0.24 * 10 ** -6  # Radius of the resin-spheres
V = math.pi * (4 / 3) * r ** 3  # Volume of the resin-spheres
T = 300.2  # Kelvin

density_resin = 1.2 * 10 ** 3
density_water = 1.0 * 10 ** 3


def E(h: float) -> float:
    return (density_resin - density_water) * g * h * V


def p(h: float, k: float) -> float:
    return math.e ** (-E(h) / (k * T))


depths = np.array([0, 18, 33, 46, 57, 71]) * 10 ** -6
spheres = np.array([131, 214, 312, 437, 625, 877])
log_spheres = np.log(spheres)

# noinspection PyTupleAssignmentBalance
fit, cov = np.polyfit(depths, log_spheres, 1, cov=True)
err = np.sqrt(np.diag(cov))

k = (density_resin - density_water) * g * V / (fit[0] * T)

print(f'k = {k:.2e}')
print(f'f(d) = {fit[0]:.2e}±{err[0]:.1e}d + {fit[1]:.2e}±{err[1]:.1e}')

fig, axs = plt.subplots(2, 2, sharex='col')
axs[0, 0].set_title('Original data')
axs[0, 0].plot(depths, spheres)
axs[0, 0].set_ylabel('# spheres')

axs[0, 1].set_title('Original data scaled')
axs[0, 1].plot(depths, log_spheres)
axs[0, 1].set_ylabel('log(# spheres)')

axs[1, 0].set_title('Linear fit on scaled data')
axs[1, 0].scatter(depths, log_spheres)
axs[1, 0].plot(depths, fit[0] * depths + fit[1])
axs[1, 0].set_xlabel('depth [m]')
axs[1, 0].set_ylabel('log(# spheres)')

axs[1, 1].set_title('Fit compared to original data')
axs[1, 1].scatter(depths, spheres)
axs[1, 1].plot(depths, math.e ** (fit[0] * depths + fit[1]))
axs[1, 1].set_xlabel('depth [m]')
axs[1, 1].set_ylabel('# spheres')

plt.savefig('export/problem09.svg')

plt.show()
