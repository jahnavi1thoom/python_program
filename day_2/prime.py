def prime(n):
    count=0
    for i in range(2,n):
        for j in range(2,n):
            if i%j==0:
               count+=1
        if(count<2):
            print(i)
n=int(input("enter a number"))
prime(n)
