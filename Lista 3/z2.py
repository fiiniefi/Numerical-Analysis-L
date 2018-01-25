def zerowe(a, b, c):
    if b < 0:
        x1 = (-b + (b**2 - 4*a*c)**1/2)/2*a
    else:
        x1 = (-b - (b**2 - 4*a*c)**1/2)/2*a
    x2 = c/(a*x1)
    return x1, x2

def naiwne_zerowe(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**1/2)/2*a
    x2 = (-b - (b**2 - 4*a*c)**1/2)/2*a
    return x1, x2


print(zerowe(1, 10, 1))
print(naiwne_zerowe(1, 10, 1))
