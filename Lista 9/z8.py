import math
import matplotlib.pyplot as pyplot

def gen_points(x, y, weight):
    n = len(x) - 1
    resx = []
    resy = []
    precision = 200
    for i in range(precision + 1):
        counx = 0
        couny = 0
        den = 0
        t = i / float(precision)
        for k in range(0, n+1):
            B = (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) * (t**k) * ((1 - t)**(n - k))
            counx += weight[k] * x[k] * B
            couny += weight[k] * y[k] * B
            den += weight[k] * B
        resx.append(counx / den)
        resy.append(couny / den)
    return resx, resy


def main():
    x = [0, 3.5, 25, 25, -5, -5, 15, -0.5, 19.5, 7, 1.5]
    y = [0, 36, 25, 1.5, 3, 33, 11, 35, 15.5, 0, 10.5]
    weight = [3, 4, 4, 3, 3, 7, 2, 1, 5, 4, 3]
    x, y = gen_points(x, y, weight)
    #print(x, '\n\n', y)
    pyplot.plot(x, y)
    pyplot.ylabel("Bezier curves")
    pyplot.show()

main()
