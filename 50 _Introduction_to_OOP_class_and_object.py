

class Student:
    roll = ''
    cgpa = ''

rafiyat = Student()
#print(isinstance(rafiyat,Student)) #cheak object
rafiyat.roll = 101
rafiyat.cgpa = 3.50

print(f"Roll : {rafiyat.roll} \nCGPA : {rafiyat.cgpa}")

rafi= Student()
rafi.roll = 102
rafi.cgpa = 3.55

print(f"Roll : {rafi.roll} , CGPA : {rafi.cgpa}")
