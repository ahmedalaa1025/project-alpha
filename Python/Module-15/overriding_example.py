class Animal:
    def sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Woof!")


dog = Dog()
dog.sound()