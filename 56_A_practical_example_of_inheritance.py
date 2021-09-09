

class Shape:
    def __init__(self,dim_1,dim_2):
        self.dim_1 = dim_1
        self.dim_2 = dim_2
    def area(self):
        print("I am area method of shape class")
class Triangle(Shape):
    #area 
    def area(self):
        area = 0.5 * self.dim_1 * self.dim_2
        print('Area of Triangle :',area)
class Rectangle(Shape):
    def area(self):
        area =   self.dim_1 * self.dim_2
        print('Area of Rectangle :',area)
T1 = Triangle(10, 20)
T1.area()
T2 = Rectangle(20, 30)
T2.area()