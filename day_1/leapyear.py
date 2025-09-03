#check whether a given year is leapyear or not
def leapyear(y):
    if (y%100!=0 and  y%4==0) or y%400==0:
        return True
    else:
        return False
y=int(input("enter a number:"))
print(leapyear(y))
    