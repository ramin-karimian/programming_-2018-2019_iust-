def hamani(n):
    d=[]
    for i in range(1,n+1):
        b=[]
        for j in range(1,n+1):
            if i==j:
                b.append(1)
            else:
                b.append(0)
        d.append(b)
    return(d)
n=eval(input('Enter your number: '))
f=hamani(n)
for i in range(len(f)):
    print(f[i])
