

class Student:
    roll = ''  
    cgpa = ''

    def __init__(self,roll,cgpa):
        self.roll = roll
        self.cgpa = cgpa
        
    def display(self):
        print(f"Roll : {self.roll} \nCGPA : {self.cgpa}")


rafiyat = Student(101,4.00)
rafiyat.display()

rafi= Student(102, 3.50)
rafi.display()

#riya= Student(103, 3.50)
#riya.display()
safi=Student(33,4.00)
safi.display()


