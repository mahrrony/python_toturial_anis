#import random
from random import randint 

n = int(input("How many time do you want to try:"))

for x in range(1,n+1):
    guess_number=int(input("Enter your guess_number between 1 to 5 : "))

    random_number =randint(1,5)
#random_number =random.random() * 100 # 0 - 100 

    if guess_number == random_number:
        print("Congratulation !! '\n' You have won ")
    else:
        print("Als !! '\n'You have lost")
        print("Random number was :",random_number)
print("Thanks for playing ")