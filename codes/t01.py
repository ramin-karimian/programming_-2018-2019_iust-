
s=0
i=0
k=0
l=0
while i<5:
    m=input("yek nomre vared konid :")
    m=eval(m) # m=float(m)
    s=s+m
    if m >15:
        k=k+1
    elif m < 10:
        l=l+1
    i=i+1
print("moadel barabar ast ba : ",s/5)
print("tedate nomarate balaye 15: ",k)
print("tedate nomarate payine 10: ",l)
