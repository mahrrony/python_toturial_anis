
"""
class Student:
    roll = ''
    cgpa = ''
    def display(self):
        print(f"Roll : {rafiyat.roll} \nCGPA : {rafiyat.cgpa}")


rafiyat = Student()
#print(isinstance(rafiyat,Student)) #cheak object
rafiyat.roll = 101
rafiyat.cgpa = 3.50
rafiyat.display()


rafi= Student()
rafi.roll = 102
rafi.cgpa = 3.55
rafi.display()"""





class Student:
    roll = ''
    cgpa = ''

    def set_value(self,roll,cgpa):
        self.roll = roll
        self.cgpa = cgpa
        
    def display(self):
        print(f"Roll : {self.roll} \nCGPA : {self.cgpa}")


rafiyat = Student()
rafiyat.set_value(1001, 3.65)
rafiyat.display()


rafi= Student()
rafi.set_value(1002, 3.50)
rafi.display()


rafit= Student()
rafit.set_value(1002, 3.50)
rafit.display()