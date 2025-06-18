

import re 

'''
pattern = r"colour"
if(re.match(pattern, "red is a colour , i love red   ccolour ")):
    print("matched")
else:
    print("Not Matched")

pattern = r"colour"
if(re.search(pattern, "red is a colour , i love red   ccolour ")):
    print("matched")
else:
    print("Not Matched")


pattern = r"red"
print(re.findall(pattern, "red is a colour , i love red   colour "))
'''
pattern =r"colour"
text = "My favourite colour is Red"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())
