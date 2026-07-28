# Question (3)

try:
  tasks = [
    "Study Python",
    "Practice NumPy",
    "Review Loops",
    "Learn Functions",
    "Solve Problems"
]

  print("===== Task Manager =====")

  print()

  for i in range(len(tasks)):
    print(i + 1 , "." , tasks[i])

  print()  

  task_number = int(input("Choose a task number:"))

  print("Choose a task number to complete:" , task_number)

  print()

  task_number_completed = tasks[task_number - 1]

  print("Task Completed:" , task_number_completed)

  print()

  tasks.remove(task_number_completed)

  new_task = input("Enter a task:")

  print("Enter a new task:" , new_task)

  tasks.append(new_task)

  print()

  print("===== Updated Tasks =====")

  print()

  for i in range(len(tasks)):
    print(i + 1 , "." , tasks[i])

except ValueError:
    print("Please enter a valid number")