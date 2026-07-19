class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major


student1 = Student("Ahmed", "Computer Engineering")

print(student1.name)
print(student1.major)