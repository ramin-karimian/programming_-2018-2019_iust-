def q(n,m):
    d=[]
    for i in range(1,n+1):
        b=[]
        for j in range(1,m+1):
            h=i*j
            b.append(h)
        d.append(b)
    return(d)
n=int(input('tedad satr ra vared konid:'))
m=int(input('tedad sotoon ra vared kionid:'))
w=q(n,m)
n=int(input('tedad satr ra vared konid:'))
m=int(input('tedad sotoon ra vared kionid:'))
p=q(n,m)
print('matris aval:',w)
print('matris dovom:',p)
z=[]
for l in range(len(w)):
    o=[]
    for x in range(len(p[0])):
        a=0
        for g in range(len(p)):
            v=w[l][g]*p[g][x]
            a=a+v
        o.append(a)
    z.append(o)
print('w*p:',z)
