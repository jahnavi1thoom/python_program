def Factorial(n):
    i=n
    fact=1
    while(i>=1):
        fact*=i
        i-=1
    return fact
n=int(input("enter a number:"))
print(Factorial(n))
        

    