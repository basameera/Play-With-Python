# Copyright (c) 2020, Sameera Sandaruwan

# Allow the code to function without numba, but discourage it
try:
    from numba import njit, jit, vectorize, int64, float64, complex128
    GOT_NUMBA = True
except ImportError:
    import warnings
    warning_text = \
        "\n\n" + "!" * 50 + "\n" + \
        "Could not import from numba, which means that some\n" + \
        "parts of this code may run MUCH more slowly.\n" + \
        "You may wish to install numba." + \
        "\n" + "!" * 50 + "\n"
    warnings.warn(warning_text)

    def _identity_decorator_outer(*args, **kwargs):
        def _identity_decorator_inner(fn):
            return fn
        return _identity_decorator_inner
    njit = _identity_decorator_outer
    jit = _identity_decorator_outer
    vectorize = _identity_decorator_outer
    int64 = int
    float64 = float
    complex128 = complex
    GOT_NUMBA = False
