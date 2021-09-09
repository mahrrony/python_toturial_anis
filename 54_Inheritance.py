"""class phone:
    def call(self):
        print("You can call")
    
    def massage(self):
        print("You call massage")
class Samsung:
    def call(self):
        print("You can call")   
    def massage(self):
        print("You call massage")    
    def photo(self):
        print("You can take photos")
p = phone()
p.call()
p.massage()
s = Samsung()
s.massage()
s.call()
s.photo()"""

class phone:
    def call(self):
        print("You can call")
    
    def massage(self):
        print("You call massage")
class Samsung(phone):
    #call,massage  
    def photo(self):
        print("You can take photos")
p = phone()
p.call()
p.massage()
s = Samsung()
s.photo()
s.call()
print(issubclass(Samsung,phone))

