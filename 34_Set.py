
"""
num_1 = {1,2,3,4,5}
num_2 = set([4,5,6,7,8])
print(num_1)
print(num_2)

num_3 =set([])
num_3.add(23)
num_3.add(26)
num_3.add(29)
num_3.add(32)
num_3.remove(26)
print(num_3)

print(5 in num_1)
print(5 not in num_1)
"""
num_1 = {1,2,3,4,5}
num_2 = set([4,5,6,7,8])

print(num_1 | num_2) #union 
print(num_1 & num_2)#intersection 
print(num_1 - num_2)
print(num_2 - num_1)