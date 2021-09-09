
class phone:
    def __init__(self):
        print("You are in phone class")
    
class Samsung(phone):
    #init 
    def __init__(self):
        super().__init__()
        print("You are in Samsung class")

S = Samsung()
