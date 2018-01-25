from numpy import sign, nan
from math import log2, cos, radians, fabs, ceil
h = 0.0000001
def bisection(a0, b0, n, f):
    if fabs(f(a0)) <= h:
        return a0
    elif fabs(f(b0)) <= h:
        return b0
    elif sign(f(a0)) == sign(f(b0)):
        return nan
    m = 0
    for i in range(n + 1):
        m = (a0 + b0) / 2.0
        if fabs(f(m)) <= h:
            return m
        if sign(f(a0)) != sign(f(m)):
            b0 = m
        else:
            a0 = m
    return m

def f(x):
    return ((x**2) - 2 * cos(((3 * x) + 1)))

print(bisection(-1, 0, ceil(log2((1/2 * (10 ** (5))))), f))
print(bisection(0, 0.5, ceil(log2((1/2 * (10 ** (5))) * (0.5))), f))
