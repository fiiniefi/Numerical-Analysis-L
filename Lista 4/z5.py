def inverse(x, n):
    res = 0.15
    for i in range(n + 1):
        print(res)
        res = res * (2 - res * x)
    return res

print(inverse(10, 8))
