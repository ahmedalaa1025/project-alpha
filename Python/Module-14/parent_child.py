class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


class Student(Person):
    pass


student1 = Student("Ahmed")

student1.introduce()