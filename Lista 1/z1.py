a = float(input("Podaj a  "))
b = float(input("Podaj b  "))
c = float(input("Podaj c  "))

x1 = (-b + (b**2 - 4*a*c)**(1/2))/2*a
x2 = (-b - (b**2 - 4*a*c)**(1/2))/2*a
print("x1 = ", x1, '\n', "x2 = ", x2)
print("f(x1) = ", a*(x1**2) + b*x1 + c)
print("f(x2) = ", a*(x2**2) + b*x2 + c)
print("Viete (x2 = c/a*x1)\tx2 = ", x2, "\tc/a*x1 = ", c/(a*x1))
