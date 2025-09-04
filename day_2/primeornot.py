def isPrime(n):
    i=1
    count=0
    while(i<=n):
        if n%i==0:
            count+=1
        i+=1
    if count>2:
        return "not a prime"
    else:
        return "is a prime"
n=int(input("enter a number"))
print(isPrime(n))