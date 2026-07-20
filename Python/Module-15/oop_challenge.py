class Shape:
  def draw(self):
    print("Drawing a shape")

class Circle(Shape):
  def draw(self):
    print("Drawing a circle")

class Rectangle(Shape):
  def draw(self):
    print("Drawing a rectangle")

shapes = [Circle() , Rectangle()]

for shape in shapes:
  shape.draw()