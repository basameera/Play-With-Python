"""Numba acc. version
"""
from numba import jit, njit
import numpy as np
import time


@njit()
def func(samples):
    length = samples.shape[0]
    mods = []
    for n in range(length):
        mods.append(samples[n]**2)


if __name__ == "__main__":

    samples = np.random.normal(0, 1, 1000000)

    st = time.time()
    mods = func(samples)
    et = time.time()

    mods = np.array(mods)
    print(et-st)
