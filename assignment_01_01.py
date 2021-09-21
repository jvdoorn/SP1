from numbers import Number
from typing import TypeVar

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0.01, 1, 100)

T = TypeVar("T", Number, np.ndarray)

gamma_vector = np.vectorize(np.math.gamma)


def factorial(a: T) -> T:
    return gamma_vector(a + 1)


def R(x: T, N: int) -> T:
    return np.square(factorial(N / 2)) / (factorial(x * N) * factorial((1 - x) * N))


def main():
    plt.ylabel('$R(x, N)$')
    plt.xlabel('$x$')

    for N in [6, 12, 24, 150]:
        plt.plot(x, R(x, N), label=f'$N={N}$')

    plt.legend()

    plt.savefig('figures/assignment_01_01.svg')
    plt.show()


if __name__ == '__main__':
    main()
