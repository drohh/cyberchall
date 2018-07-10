selnumsfi = open("finalnums.txt", "r")

for x in selnumsfi:
    newfile = open("gettosearching/"+str(x).rstrip("\n")+".txt","w")
    print(x)
    newfile.close()