def element_frequency(l):
    ll=set()
    for i in range(len(l)):
        e_count=0
        for j in range(i,len(l)):
            if l[i] in ll:
                continue
            elif l[i]==l[j]:
                e_count+=1
        ll.add([l[i],e_count])
    return ll
l=list(map(int,input().split()))
print(element_frequency(l))