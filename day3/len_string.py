def count_len(l):
    count=0
    for i in l:
        count+=1
    return count
def compare(l,l2):
    if len(l)!=len(l2):
        return "not equal"
    else:
        for i in range(len(l)):
            if l[i]!=l2[i]:
                return "not equal"
            else:
                return "equal"
def concatenate(l,l2):
    return l+l2



l=input()
l2=input()
print("len of string:",count_len(l))
print(compare(l,l2))
print(concatenate(l,l2))
