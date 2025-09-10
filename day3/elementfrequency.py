def element_frequency(l):
    ll=[]
    for i in range(len(l)):
        e_count=0
        for j in range(i,len(l)):
            if l[i] in ll[0]:
                continue
            elif l[i]==l[j]:
                e_count+=1
        ll.append([l[i],e_count])
    return ll
l=list(map(int,input().split()))
print(element_frequency(l))