class Vehicle:
  def __init__(self, brand):
    self.brand = brand

  def show_brand(self):
    print("Brand:", self.brand)

class Car(Vehicle):
  def __init__(self, brand, model):
    super().__init__(brand)
    self.model = model

  def show_model(self):
    print("Model:", self.model)

car1 = Car("Toyota", "Corolla")

car1.show_brand()
car1.show_model()
