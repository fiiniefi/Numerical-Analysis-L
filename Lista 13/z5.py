import math

def Romberg(a, b, f, n):
    R = []
    R.append((1/2) * (b-a) * (f(a) + f(b)))
    #print(R[0])
    for i in range(1, n+1): #pierwsza kolumna
        M = 0
        h = (b-a)/(2**(i-1))
        for j in range (1, (2**(i-1))+1):
            M += f(a + (1/2)*(2*j - 1)*h)
        M *= h
        #print(h)
        R.append((1/2) * (R[i-1] + M))
        #print(R[i])
    for i in range(1, n+1):
        for j in range(0, ((n+1)-i)):
            R[j] = ((4**i)*R[j+1] - R[j])/((4**i)-1)
            #print(R[j])
    return R[0]

def fun1(x):
    return ((2018*(x**5)) + (2017*(x**4)) - (2016*(x**3)) + 2015*x)

def fun2(x):
    return (1 / (1 + (x**2)))

def fun3(x):
    return ((math.cos(2*x))/x)

def main():
    print('%.19f' % Romberg(-5, 3, fun1, 15))
    print('%.19f' % Romberg(-5, 5, fun2, 15))
    print('%.19f' % Romberg(math.pi, 15, fun3, 15))

main()
