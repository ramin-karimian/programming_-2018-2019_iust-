x=int(input('adad ra vared konid'))
p=0
i=0
while x!=0:
    d=x//10
    h=x-d*10
    i=i+1
    p=p+h
    x=x//10
print('tedad argham:',i)
print('majmoo argham:',p)
