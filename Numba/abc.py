import numpy as np
import time

if __name__ == "__main__":
    
    samples = np.random.normal(0, 1, 1000000)
    length = samples.shape[0]

    mods = []

    st = time.time()

    for n in range(length):
        mods.append(samples[n]**2)
    
    et = time.time()

    mods = np.array(mods)
    print(et-st)