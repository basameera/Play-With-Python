# Python Numba

> Goal : Make a python module that works with/without numba installed.

## Tasks

- [ ] Make two envs with and without numba installed (`conda create -n pth37 python=3.7 pip`)

## Log

`conda install numba`

### Better use:
Numba works after compilation. So, it's better to use with functions that get called over and over again (e.g. a function inside a loop)



```python
from numba import jit
import numpy as np
import time

x = np.arange(100).reshape(10, 10)

@jit(nopython=True)
def go_fast(a):  # Function is compiled and runs in machine code
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace


# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed (with compilation) = %s" % (end - start))

# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed (after compilation) = %s" % (end - start))
```

## References

http://numba.pydata.org/numba-doc/latest/user/5minguide.html
https://thedatafrog.com/en/articles/make-python-fast-numba/
https://kratzert.github.io/2017/09/12/introduction-to-the-numba-library.html


