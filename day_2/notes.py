def Notes(a):
    count=0
    while(a>0):
       if a>=10 and a<50:
           count+=1
           a-=10
       elif a>=50 and a<100:
           count+=1
           a-=50
       elif a>=100 and a<500:
           count+=1
           a-=100
       elif a>=500 and a<2000:
           count+=1
           a-=500
       elif a>=2000:
           count+=1
           a-=2000
    return count
a=int(input("enter amount"))
print("total number of notes:",Notes(a))

    
    

