from math import exp, fabs
from numpy import sign
def f(x):
    return ( (x * exp(-x)) - 0.06064 )

def main():
    alpha = 0.0646926359947960
    a = a0 = 0
    b = b0 = 1
    mn = 0
    for i in range(16):
        mn = ( (b + a) / 2 )
        if sign(f(a)) != sign(f(mn)):
            b = mn
        else:
            a = mn
        print("Dla n = ", i, " przybliżenie miejsca zerowego wynosi\t\t", mn, sep = "")
        print("Dla n = ", i, " błąd rzeczywisty wynosi\t\t\t", fabs(alpha - mn), sep = "")
        print("Dla n = ", i, " oszacowanie wynosi\t\t\t\t", (2**(-i-1)) * (b0 - a0), sep = "")


main()
