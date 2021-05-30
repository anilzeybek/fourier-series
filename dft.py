from scipy.linalg import dft
from numpy import conj


def find_DFT(N, s):
    return dft(N) @ s


def find_IDFT(N, s):
    return 1 / N * conj(dft(N)) @ s


find_DFT(4, [1, 1999 / 2000, 1998 / 2000, 1997 / 2000])

find_IDFT(4, [6, -2 + 2j, -2, -2 - 2j])
