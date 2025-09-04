def Armstrong():
    
    
    for i in range(1,1000):
        temp=i
        s=0
        while(i!=0):
           r=i%10
           s+=r*r*r
           i=i//10
        if s==temp:
            print(temp)
        
Armstrong()