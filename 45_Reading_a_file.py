

file = open("45_student.txt","r")
"""
#print(file.readable())
#text=file.read()
#print(text)
#size=len(text)
##print(size)
#line = file.readlines()
line = file.readlines()[2]
print(line)
"""
for line in file:
    print(line)
file.close()


'''
Rony is a student .
He reads in class ten in Al Helal  Isalami Academy And College .  He lives in Bangladesh with his family .  '''