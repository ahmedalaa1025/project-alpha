file = open("Python/Module-11/students.txt", "w")

file.write("Ahmed\n")
file.write("Ali\n")
file.write("Sara\n")

file.close()

file = open("Python/Module-11/students.txt", "a")

file.write("Omar\n")

file.close()

with open("Python/Module-11/students.txt", "r") as file:
  content = file.read()
  print(content)
