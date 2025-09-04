def palindrome(n):
    temp=n
    s=""
    while(n!=0):
        r=n%10
        s=s+str(r)
        n=n//10

    if s==str(temp):
        return "Palindrome"
    else:
        return "not a palindrome"
n=int(input("enter a number"))
print(palindrome(n))
        
        
        