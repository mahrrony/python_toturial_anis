

text = "rony"
print(text[0])

"""num_2 = int(input("Enter a number : "))
result  = 200/ num_2
print(result)

try:
    list=  [ 20, 10,0,30,40]
    result= list[0]/list[7]
    print(result)
    print("DONE")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Index Error")

print("Successful")
"""

try:
    list=  [ 20, 10,0,30,40]
    result= list[0]/list[7]
    print(result)
    print("DONE")
except ZeroDivisionError:
    print("Dividing by zero is not possible") 
finally: #ফাইনালি কিওয়ার্ড কোন এক্সেপশন ক্লিয়ারনা করতে পারলে তার পরের কোড রানকরার জন্য ব্যবহার করতে হয়
    print("Successful")


