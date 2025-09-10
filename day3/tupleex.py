def tuple_ex(l):
    m=0
    for i in range(len(l)):
        print(l[i][0])
        if l[i][2]>75:
            print(l[i][0],"is having marks graeter than 75")
        if l[i][2]>m:
            m=l[i][2]
    print("maximum markss:",m)
        



l=[]
for i in range(6):
   name=input()
   rollno=int(input())
   marks=int(input())
   l.append((name,rollno,marks))


tuple_ex(l)