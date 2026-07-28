# Final Python Project

students = [
    ["Ahmed", [85, 90, 78]],
    ["Omar", [60, 55, 70]],
    ["Mariam", [95, 92, 98]],
    ["Youssef", [40, 50, 45]],
    ["Sara", [88, 84, 91]]
]

print("===== University Student Management System =====")

print()

print("===== Student Report =====")

print()

for student in students:
  print("Name:" , student[0])
  print("Grades:" , student[1])
  average = sum(student[1]) / len(student[1])
  print("Average:" , average)
  if (average >= 60):
    print("Status: Pass")
  else:
    print("Status Fail")
  print()
  print("----------------------------")
  print()

name = input("Enter a name:")

print("Enter student name: " , name)

print()

print("===== Student Information =====")

print()

found = False

for student in students:
  if (student[0] == name):
    found = True
    print("Name:" , name)
    print("Grades:" , student[1])
    average = sum(student[1]) / len(student[1])
    print("Average:" , average)
    if (average >= 60):
      print("Status: Pass")
    else:
      print("Status Fail")
    break

if not found:
  print("Student is not found.")

print()

print("============================")

print()

print("===== Exam Statistics =====")

print()

pass_count = 0
fail_count = 0

for student in students:
  average = sum(student[1]) / len(student[1])
  if (average >= 60):
    pass_count += 1
  else:
    fail_count += 1

print("Passed Students:" , pass_count)
print("Failed Students:" , fail_count)

print()

maximum_average = sum(students[0][1]) / len(students[0][1])
maximum_student_average = students[0][0]

for i in range(1 , len(students)):
  average = sum(students[i][1]) / len(students[i][1])
  if (average > maximum_average):
    maximum_average = average
    maximum_student_average = students[i][0]

print("Top Student:" , maximum_student_average)
print("Average:" , maximum_average)

print()

print("============================")

print()

print("Program Finished Successfully.")
