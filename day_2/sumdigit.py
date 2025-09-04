def sumdigit(n):
    s=0
    while(n!=0):
      r=n%10
      s+=r
      n=n//10
    return s
n=int(input("enter a number:"))
print("sum of digits:",sumdigit(n))