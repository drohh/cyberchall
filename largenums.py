import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def nobadend(num):
    if num % 10 == 5 or num % 2 == 0:
        return False
    return True


myfile = open("output.txt", "w")


x = 3
while 1:
    if nobadend(x) and not is_prime(x):
        myfile.write(str(x)+"\n")
    x += 1