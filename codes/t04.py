N=int(input("n ra vared konid"))

s=0
for x in range (1,N+1):
    p=1
    for i in range (1,x+1):
        p=p*i
    s=s+p
print(s)
