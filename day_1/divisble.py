def Divisible(d):
    if d%5==0 and d%11==0:
        return True
    else:
        return False
d=int(input("enter a number"))
print(Divisible(d))