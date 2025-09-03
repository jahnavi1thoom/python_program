name=input("enter student name:")
num=int(input("enter student number"))
marks1=float(input("enter marks of  subject1:"))
marks2=float(input("enter marks of  subject2:"))
marks3=float(input("enter marks of  subject3:"))
total=marks1+marks2+marks3
print("name:",name," student number:",num)
print("total marks:",round(total,2))
avg=total/3
print("average of total:",round(avg,2))



        