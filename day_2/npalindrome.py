
def palindrome():
    
    for i in range(1,100):
        temp=i
        s=""
        while(i!=0):
           r=i%10
           s=s+str(r)
           i=i//10

        if s==str(temp):
            print(temp)

    