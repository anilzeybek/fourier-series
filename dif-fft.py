from scipy.linalg import dft
import numpy as np


def DIF_FFT(N, s):
    W_N = np.exp(-1j * (2 * np.pi / N))

    p = [s[i] + s[i + N // 2] for i in range(N // 2)]
    q = [(s[i] - s[i + N // 2]) * (W_N ** i) for i in range(N // 2)]

    P = dft(N // 2) @ p
    Q = dft(N // 2) @ q

    result = []
    for i in range(N // 2):
        result.append(P[i])
        result.append(Q[i])

    return result


def DIF_radix2(N, s):
    if N == 2:
        a = s[0] + s[1]
        b = s[0] - s[1]
        return [a, b]

    W_N = np.exp(-1j * (2 * np.pi / N))

    p = [s[i] + s[i + N // 2] for i in range(N // 2)]
    q = [(s[i] - s[i + N // 2]) * (W_N ** i) for i in range(N // 2)]

    r1 = DIF_radix2(N // 2, p)
    r2 = DIF_radix2(N // 2, q)

    return r1 + r2


DIF_FFT(8, [1, 1, -1, -1, -1, 1, 1, -1])

r = DIF_radix2(8, [1, -1, -1, -1, 1, 1, 1, -1])
# Don't forget to rearrange it!!!!
# 0, 4, 2, 6, 1, 5, 3, 7
