tab = [1, 1/5]

for i in range (50):
    temp = tab[1]
    tab[1] = (26/5) * tab[1] - tab[0]
    tab[0] = temp
    print("Wedlug wzoru: x", i+2, " = ", tab[1])
    print("Realnie: x", i+2, " = ", 1/(5**(i+2)))
