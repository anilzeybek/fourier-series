from scipy.linalg import dft
from numpy import conj
import numpy as np


def DIT_FFT(N, s):
    even_part = [s[i] for i in range(len(s)) if i % 2 == 0]
    odd_part = [s[i] for i in range(len(s)) if i % 2 != 0]

    F = dft(N // 2) @ even_part
    G = dft(N // 2) @ odd_part

    W_N = np.exp(-1j * (2 * np.pi / N))

    X = []
    for i in range(N // 2):
        X.append(F[i] + (W_N ** i) * G[i])

    for i in range(N // 2):
        X.append(F[i] - (W_N ** i) * G[i])

    return X


def DIT_radix2(N, s):
    pass


def inverse_DIT_FFT(N, s):
    even_part = [s[i] for i in range(len(s)) if i % 2 == 0]
    odd_part = [s[i] for i in range(len(s)) if i % 2 != 0]

    F = dft(N // 2) @ even_part
    G = dft(N // 2) @ odd_part

    W_N = np.exp(-1j * (2 * np.pi / N))

    X = []
    for i in range(N // 2):
        X.append(F[i] + conj(W_N ** i) * G[i])

    for i in range(N // 2):
        X.append(F[i] - conj(W_N ** i) * G[i])

    return [x / N for x in X]


print(DIT_FFT(4, [1, 2, 3, 4]))

print(inverse_DIT_FFT(4, [10, -2 + 2j, -2, -2 - 2j]))
