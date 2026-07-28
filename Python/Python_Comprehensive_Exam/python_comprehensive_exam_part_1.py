# Question (1)

students = [
    ["Ahmed", 85],
    ["Omar", 62],
    ["Mariam", 95],
    ["Youssef", 48],
    ["Sara", 76]
]

print("===== Student Performance Report =====")

print()

for i in range(len(students)):
  if (students[i][1] >= 90):
    print(students[i][0] , ":" , students[i][1] , "-" , "Excellent")
  elif (students[i][1] >= 80):
    print(students[i][0] , ":" , students[i][1] , "-" , "Very Good")
  elif (students[i][1] >= 70):
    print(students[i][0] , ":" , students[i][1] , "-" , "Good")
  elif (students[i][1] >= 60):
    print(students[i][0] , ":" , students[i][1] , "-" , "Pass")
  else :
    print(students[i][0] , ":" , students[i][1] , "-" , "Fail")

print()    

print("===== Statistics =====")

print()

maximum_grade = students[0][1]
maximum_student = students[0][0]

for i in range(1 , len(students)):
  if (students[i][1] > maximum_grade):
    maximum_grade = students[i][1]
    maximum_student = students[i][0]

print("Highest Grade:" , maximum_grade)
print("Top Student:" , maximum_student)

print()

minimum_grade = students[0][1]

for i in range(1 , len(students)):
  if (students[i][1] < minimum_grade):
    minimum_grade = students[i][1]

print("Lowest Grade:" , minimum_grade)

print()

total = 0
count = 5

for i in range(len(students)):
  total += students[i][1]

average = total / count

print("Average Grade:" , average)

print()

passed_students = 0
failed_students = 0

for i in range(len(students)):
  if (students[i][1] >= 50):
    passed_students += 1
  else:
    failed_students += 1

print("Passed Students:" , passed_students)
print("Failed Students:" , failed_students)

print()

print("===== Passed Students =====")

print()

for student in students:
  if (student[1] >= 50):
    print(student[0])

print()

print("===== Failed Students =====")

print()

for student in students:
  if (student[1] < 50):
    print(student[0])
