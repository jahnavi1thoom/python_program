def sumfirstlast(n):
    l=[]
    while (n!=0):
        r=n%10
        l.append(r)
        n=n//10
    nl=len(l)
    s=l[0]+l[n-1]
    return s
n=int(input("enter a digit:"))
print(sumfirstlast(n))