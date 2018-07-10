import os
from random import randint

diry = "/Users/dcr/PycharmProjects/primefun/gettosearching/"

passes = []
passfile = open("randopasses.txt", "r")

for x in passfile:
    passes.append(x.rstrip("\n"))

print(passes)

i = 0
#ipi = 1

for filename in os.listdir(diry):
    #ip = "10.%s.%s.%s"
    curr = open(diry + "/" + filename, "w")
    curr.write("10.%s.%s.%s" % (str(randint(1, 255)),str(randint(1, 255)),str(randint(1, 255))) + "\n" + passes[i])
    curr.close()
    i+=1
    #ipi += 1