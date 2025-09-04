def weekAndDay(n):
    if n==0:
        return "Sunday:" 
    elif n==1:
        return "Monday"
    elif n==2:
        return "Tuesday"
    elif n==3:
        return "Wednesday"
    elif n==4:
        return "Thursday"
    elif n==5:
        return "Friday"
    elif n==6:
        return "Saturday"
    
n=int(input("enter a week day:"))
print(weekAndDay(n))

