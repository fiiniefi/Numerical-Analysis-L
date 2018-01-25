h = 0.001
def v1(x):
    return ((5*(x+h) * (x+h) - 5*(x*x))/h)

def v2(x):
    return ((5*(x+h) * (x+h) - 5*(x-h) * (x-h))/(2*h))

for i in range (100):
    print("Wersja gorsza:", v1(i))
    print("Wersja lepsza:", v2(i))
    print("Wersja prawdziwa:", 10*i)

    #Uzywam 5x^2
