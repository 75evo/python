st="nneigheigh"
snd = "neigh"
x = {v: k for k, v in enumerate(snd)}
print(x)

for i in range(len(st)):
    print(str(st[i]) + str(x.get(st[i])))

