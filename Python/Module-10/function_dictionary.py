def print_student(student):
    for key, value in student.items():
        print(key, ":", value)


data = {
    "name": "Ahmed",
    "age": 20,
    "major": "Computer Engineering"
}

print_student(data)