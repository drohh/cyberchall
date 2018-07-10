import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

myst = [293339,649739,31513,1000669,331777,739391,904117,155521,274177]

for x in myst:
    print(is_prime(x))