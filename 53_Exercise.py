

class triangle :
    base = ""
    height=""

    def __init__(self,base ,height):
        self.base =  base 
        self.height=height 
    def display(self):
        Area =.5 * self.base * self.height
        print("Area = ",Area)
        
calculate_area_1= triangle(10, 20)
calculate_area_1.display()

calculate_area_2= triangle(20,30)
calculate_area_2.display()