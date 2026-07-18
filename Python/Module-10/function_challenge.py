def count_items(students):
  return len(students)

numbers = [10, 20, 30]

print(count_items(numbers))

def make_upper(text):
  return text.upper()

print(make_upper("python"))

def print_student(student):
  for key , value in student.items():
    print(key, ":", value)

data = {
    "name": "Ahmed",
    "age": 20
}

print_student(data)

