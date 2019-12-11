n=list()
N=int(input('tedad adad ra vared konid:'))
for i in range(N):
    b=int(input('adad ra vared konid:'))
    n.append(b)

M=int(input(" yek adad vared konid : "))

for i in range(N-1,-1,-1):
    if M==n[i]:
        del n[i]

print(n)

