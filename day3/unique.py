def unique_ele(l):
    count=0
    l1=[]
    for i in range(len(l)):
        count=0
        for j in range(len(l)):
            if l[i]==l[j]:
                count+=1
        if count==1:
            l1.append(l[i])

    return l1
l=list(map(int,input().split()))
print(unique_ele(l))