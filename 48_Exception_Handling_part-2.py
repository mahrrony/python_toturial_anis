
'''
try:
    num_1 = int(input("Enter First Number : "))
    num_2 = int(input("Enter Second Number : "))

    result = num_1/num_2
    print(result)

    """
except ValueError:
    print("You have to insert only integer.")
except ZeroDivisionError:
    print("You can not divide a number by Zero.")
"""

except (ValueError,ZeroDivisionError):
    print("You have entered incorrect valu ") 
finally:
    print('Done')


'''

def voter (age):
    if age <18:
        raise  ValueError("Invalid Voter")
    return "You are allowed to vote"

try:
    print(voter(4))
except ValueError as Error: #as ....set a name and print this 
    print(  Error  )

