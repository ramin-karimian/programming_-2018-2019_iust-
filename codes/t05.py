n=list()
q=list()
N=int(input('tedad adad ra vared konid:'))
for i in range(N):
    b=int(input('adad ra vared konid:'))
    n.append(b)

for j in range(N):
    for c in range(j+1,N):
        if n[j]==n[c]:
            if n[c] not in q:
                q.append(n[c])
print('adad tekrari:',q)
