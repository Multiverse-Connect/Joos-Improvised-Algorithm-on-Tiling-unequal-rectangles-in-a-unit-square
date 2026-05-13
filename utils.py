import math


def close(a, b, eps=1e-12):
    return math.isclose(a, b, abs_tol=eps)