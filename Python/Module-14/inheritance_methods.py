class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def study(self):
        print(self.name, "is studying", self.major)


student1 = Student("Ahmed", "Computer Engineering")

student1.introduce()
student1.study()