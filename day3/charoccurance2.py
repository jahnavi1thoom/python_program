from collections import Counter
def char_occurance(l):
    l2=Counter(l)
    s=""
    for key,value in l2.items():
        s+=key
        s+=str(value)
    return s
l=input()
print(char_occurance(l))
