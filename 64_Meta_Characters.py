

import re

pattern = r"colo..r"
if re.match(pattern,"col,obr"):
    print("Matched")
else:
    print("Not Matched")


pattern = r"^colo...r$"
if re.match(pattern,"coloppqr"):
    print("Matched")
else:
    print("Not Matched")

pattern = r"a*"
if re.match(pattern,"coloppqr"):
    print("Matched")

pattern = r"(ab)*"
if re.match(pattern,"coloppqr"):
    print("Matched")
pattern = r"a+"
if re.match(pattern,"colopapqr"):
    print("Matched")
else:
    print("Not Matched")


pattern = r"ice(-)?cream"
if re.match(pattern,"icecream"):
    print("Matched")
else:
    print("Not Matched")

pattern = r"a{1,3}$"
if re.match(pattern,"aaa"):
    print("Matched")
else:
    print("Not Matched")