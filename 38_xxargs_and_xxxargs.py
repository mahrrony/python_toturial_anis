

#xargs
def student(*details):
    print(details)
    #print(details[0])

student(101,"Anis")
student(102,"jannat",3.75)

'''
def add(num_1,num_2):
    sum = num_1 + num_2 
    return sum 

result = add(30, 35)
print("Aswer is : ",result)


def add(numbers):
    sum =0
    for num in numbers:
        sum = sum + 1 

    print("Aswer is : ",sum)

add(30,35)
add(23,21,23)
add(23,56,344,5)
print("Aswer is : ",sum)
'''
#xxargs

def student(**details):
    print(details)
  #  print(details["id"])

student(id=101,name="rony",study='AHIA&C')
#fffwgerh