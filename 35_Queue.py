
from collections import deque
#FIFO = frist in frist out 

bank = deque(["Rony","karim","Rasmika"])
bank.popleft()
print(bank)

if not bank:
    print("No person is left")
