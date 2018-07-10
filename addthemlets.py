from random import randint
import string

alph = list(string.ascii_lowercase)

selnumsfi = open("selectednums.txt", "r")
newfile = open("finalnums.txt", "w")

for line in selnumsfi:
    #print(line.rstrip("\n"))
    #print(alph[randint(0,25)]+line)
    newfile.write(alph[randint(0,25)]+line)