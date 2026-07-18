students = ["Ahmed", "Ali", "Sara"]

for name in students:
  print(name)

for index , nickName in enumerate(students,start = 1):
    print(index,nickName)

student = {
    "name": "Ahmed",
    "age": 20,
    "major": "Computer Engineering"
}

for key , value in student.items():
   print(key, ":", value)

word = "Python"

for letter in word:
   print(letter)
   