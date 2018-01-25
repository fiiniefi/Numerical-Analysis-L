def pi(rg):
    suma = 0
    for i in range (rg):
        suma += ((-1)**i)/(2*i + 1)
    suma *= 4
    return suma

print(pi(20000000))
