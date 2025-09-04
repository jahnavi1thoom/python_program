n=int(input("enter a number:"))
s=0
temp=n

fact=1  
while(n!=1):
    r=n%10
    fact*=r
    s+=fact
    n=n//10
if temp==s:
    print("strong number")
else:
    print("not a strong number")