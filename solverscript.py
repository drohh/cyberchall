import os
import math
import re

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

diry = "/Users/dcr/PycharmProjects/primefun/gettosearching/"

for filename in os.listdir(diry):
    numinfile = re.sub('[^\d]', '', filename)
    if (is_prime(int(numinfile)) and is_prime(int(numinfile[::-1]))):
        print(filename)
