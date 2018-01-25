def sqrt(a, n):
    res = 10
    for i in range(n + 1):
        print(res)
        res = (0.5 * (res + (a / res)))
    return res

print(sqrt(6, 5))
