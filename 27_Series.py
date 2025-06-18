

#1+2+3+.....+n
n = int(input("Enter the last number : "))
sum = 0
for x in range(1,n+1,1):
    sum = sum + x
print(sum)



#define a list of strings
D = []
# print the list of strings
D.append("Eve")
D.append("Alice")
D.append("Bob")
print(D)


# loop over the names list, and
# print each string one at a time
for name in D:
   print(name)


# add a name to the list
D.append("Charlie")

# check if the list contains a string
if "Bob" in D:
     print("Bob is here")


# add another string list to it
more_names = ["Ivan", "Gerth"]
D = D + more_names

# sort the list
D.sort()

# join the strings in the list by a comma
comma_separated = ", ".join(D)

print(comma_separated)
"""

"""
# 1 +2 + 3....... + n 
n = int(input("Enter the last number : "))
sum = 0 
for x in range(1,n+1,1):
    sum = sum + x 
print(sum)

#odd_sum
# 1 +3 + 5....... + n 
n = int(input("Enter the last number : "))
sum = 0 
for x in range(1,n+1,2):
    sum = sum + x 
print(sum)

#even_sum
# 2 + 4 + 6....... + n 
n = int(input("Enter the last number : "))
sum = 0 
for x in range(2,n+1,2):
    sum = sum + x 
print(sum)


# 1^2 +2^2 + 3^2 +....... + n^2 
n = int(input("Enter the last number : "))
sum = 0 
for x in range(1,n+1,1):
    sum = sum + x 
print(sum)