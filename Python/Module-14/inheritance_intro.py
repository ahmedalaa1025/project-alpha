class Person:
    def speak(self):
        print("I can speak.")

class Student(Person):
    pass

student = Student()

student.speak()