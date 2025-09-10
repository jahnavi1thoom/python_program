from collections import Counter
def all_occurance(l):
    l1=[]
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
    for i in range(len(l2)):
        count=0
        for j in range(len(l)):
            if l2[i]==l[j]:
                count+=1
        l1.append(l2[i])
        l1.append(count)
    return "".join(map(str,l1))
l=input()
print(all_occurance(l))
                
