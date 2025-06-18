


import re
pattern = r"[A-Z][a-z][0-9]"
if re.match(pattern,"Pr923"):
    print("Matched")
else:
    print("Not Matched")


