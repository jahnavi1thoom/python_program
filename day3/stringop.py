def alphabet(l):
    count=0
    for i in l:
        if i.isalpha():
            count+=1
    return count
def digit(l):
    count=0
    for i in l:
        if i.isdigit():
            count+=1
    return count
def special_char(l):
    count=0
    for i in l:
        if i.isalnum():
            count+=1
    return len(l)-count
l=input()
print("no of alphabets:",alphabet(l))
print("no of digits:",digit(l))
print("special characters:",special_char(l))

