class Book:
  def __init__(self,title,author):
    self.title = title
    self.author = author

  def display(self):
    print("Title: ", self.title)
    print("Author: ", self.author)

book1 = Book("Clean Code", "Robert C. Martin")

book1.display()