"""
Simulation for problem 01 of SP1.
"""
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial


def R(N: int) -> Tuple[np.ndarray, np.ndarray]:
    # Generate the x array
    x = np.arange(0, N + 1, dtype=np.float64)
    # Probability
    p = 0.5
    # Calculate R
    y = factorial(N - 1) * np.power(p, N - 1) / (factorial(x) * factorial(N - x))

    return x, y


if __name__ == '__main__':
    for N in [6, 12, 24, 170]:
        x, y = R(N)
        plt.plot(x, y, label=f'N={N}')

    plt.legend()
    plt.xlabel(r'$0 \leq x \leq N$')
    plt.ylabel(r'$R(x, N)$')
    plt.savefig('export/problem01.svg')
    plt.show()
