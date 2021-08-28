

def calculate(a,b):
    return a*a + 2*a*b + b*b

print(calculate(2, 3))

#result =  (lambda parameter : expression)(parameter)
result=(lambda a,b : a*a + 2*a*b + b*b)(2,3)
print(result)

def cube(x):
    return x*x*x
print(cube(3))

Cube=(lambda a : a*a*a)(3)
print(Cube)