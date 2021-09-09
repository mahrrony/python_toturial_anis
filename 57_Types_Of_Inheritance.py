

"""class A:
    def display_1(self):
        print("I am inside A class")
class B(A):
    def display_2(self):
        super().display_1()
        print("I am inside B class")
class C(B):
    def display_3(self):
        super().display_2()
        print("I am inside C class")

obl = C()
obl.display_3()
"""
class A:
    def display(self):
        print("I am inside A class")
class B:
    def display(self):
        print("I am inside B class")
class C(A,B):
    pass

obl = C()
obl.display()
