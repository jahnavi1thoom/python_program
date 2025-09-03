#check a given character is vowel or consonent
def VowelOrConsonent(a):
    l=['a','e','i','o','u','A','E','I','O','U']
    if a in l:
        return "vowel"
    else:
        return "consonent"
a=input("enter a character:")
print(VowelOrConsonent(a))