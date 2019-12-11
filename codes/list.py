l=[] ## ya l=list()

for i in range(5):
    l.append(i*10)

l1=list(l)

for i in range(len(l1)):
    if l1[i] >= 20:
        l1[i]=0

l3=list(l)

del l3[1]
