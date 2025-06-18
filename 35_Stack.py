
books = []                #LIFO last in frist out 
books.append("Learn C ")
books.append("Learn C++ ")
books.append("Learn Java ")
books.append("Learn Python ")
print(books)


books.pop()
#print(books)
print("Now the top book is : ",books[-1])

books.pop()
print("Now the top book is : ",books[-1])

books.pop()
print("Now the top book is : ",books[-1])

books.pop()
if not books:
    print("No books left ")