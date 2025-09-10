def del_specified_elemnt(l,a):
    for i in range(len(l)):
        if i==a:
            continue
        print(l[i],end=" ")
l=list(map(int,input().split()))
a=int(input())
del_specified_elemnt(l,a)