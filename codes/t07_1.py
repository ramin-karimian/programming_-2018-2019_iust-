def nn(n):
    b=[]
    for i in range(1,n+1):
        a=[]
        for j in range(1,n+1):
            m=i*j
            a.append(m)
        b.append(a)
    return (b)

c=nn(3)
print(c)
