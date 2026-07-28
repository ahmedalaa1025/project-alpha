# Question (5)

books = [
    ["Python Basics", True],
    ["Java OOP", False],
    ["Data Structures", True],
    ["Algorithms", True],
    ["Database Systems", False]
]

print("===== Library Books =====")

print()

available_count = 0
borrowed_count = 0

for book in books:
  if (book[1] == True):
    print(book[0] , ":" , "Available")
    available_count += 1
  else:
    print(book[0] , ":" , "Borrowed")
    borrowed_count += 1

print()

print("===== Statistics =====")

print()

print("Available Books:" , available_count)
print("Borrowed Books:" , borrowed_count)

print()

book_name = input("Enter a book name:")

print("Enter book name:" , book_name)

found = False

for book in books:
  if (book[0] == book_name):
    found = True
    if (book[1] == True):
      book[1] = False
      print("Book Borrowed Successfully")
    else:
      print("Book is already Borrowed")
    break

if not found:
  print("Book is not found")

print()

print("===== Updated Library =====")

print()

for book in books:
  if (book[1] == True):
    print(book[0] , ":" , "Available")
  else:
    print(book[0] , ":" , "Borrowed")
