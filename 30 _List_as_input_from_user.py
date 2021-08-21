
"""
n = input("Enpur a text of number :")

list = n.split()
sum = 0

for num in list : 
    sum = sum + int(num)
    print(sum)
"""

number_of_words = 0 
number_of_letters = 0
number_of_digits = 0 

text = input("Enter a text of number :")
for x in text:
   # x.lower()
    if x >= 'a' and  x <=  'z':
        number_of_letters= number_of_letters +1

    elif x >= '0' and x <= '9':
        number_of_digits = number_of_digits +1

    elif x ==' ':
        number_of_words = number_of_words +1

print("Number of didits : ",number_of_digits)
print("Number of letters : ",number_of_letters)
print("Number of words : ",number_of_words)


