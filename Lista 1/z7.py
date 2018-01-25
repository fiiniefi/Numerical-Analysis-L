import math
import numpy as np

tab = [np.float32(math.log(8/7))]
for i in range (1, 21):
    tab = np.append(tab, np.float32(1/i - 7 * tab[i-1]))
    print(tab[i])
print(tab[20] + 7 * tab[19])
