

text = "rony"
print(text[0])

"""num_2 = int(input("Enter a number : "))
result  = 200/ num_2
print(result)
"""
try:
    list=  [   20, 10  ,30,40]
    result= list[0]/list[1]
    print(result)
    print("DONE")
except ZeroDivisionError:
    print("Dividing by zero is not possible")



