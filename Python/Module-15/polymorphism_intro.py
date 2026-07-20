class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Woof!")


class Cat(Animal):
    def sound(self):
        print("Meow!")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()