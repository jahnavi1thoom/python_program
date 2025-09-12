class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("name of the student:",self.name)
        print("rollno oof the student:",self.rollno)
        print("marks of the student:",self.marks)

ob1=Student('jahnavi',82,98)
ob1.display()
ob2=Student('sam',86,87)
ob2.display()
