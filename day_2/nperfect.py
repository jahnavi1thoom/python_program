n=int(input())
l=[]
for i in range(1,n):
    s=0
    for j in range(1,n):
        if i%j==0:
            s+=j
    if s==i:
        l.append(i)
print(l)
