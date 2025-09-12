from abc import ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("area:",self.length*self.breadth)
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area:",3.14*self.radius*self.radius)
ob1=Circle(4)
ob1.area()
ob2=Rectangle(6,8)
ob2.area()
