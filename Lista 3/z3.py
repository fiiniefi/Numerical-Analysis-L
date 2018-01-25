def zerowe_cardano(q, r):
    return ((r + (q**3 + r**2)**1/2)**1/3) + ((r - (q**3 + r**2)**1/2)**1/3)

print(zerowe_cardano(1000, 1000))
