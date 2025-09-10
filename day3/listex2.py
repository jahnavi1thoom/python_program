def listex2(l):
    for i in range(len(l)):
        if l[i]<0:
            print(l[i])
l=list(map(int,input().split()))
listex2(l)