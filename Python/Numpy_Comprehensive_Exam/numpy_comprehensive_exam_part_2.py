# Question (2)

import numpy as np

grades = np.array([
    [85, 90, 78],
    [60, 55, 70],
    [95, 92, 98],
    [40, 50, 45],
    [88, 84, 91]
])

print("===== Student Grades Report =====")

print()

student_average = np.mean(grades , axis = 1)

print("Student Average:" , student_average)

print()

student_status = np.where(student_average >= 60 , "Pass" , "Fail")

print("Student Status:" , student_status)

print()

subject_average = np.mean(grades , axis = 0)

print("Subject Average:" , subject_average)

print()

highest_grade_per_subject = np.max(grades , axis = 0)

print("Highest Grade Per Subject:" , highest_grade_per_subject)

print()

print("Grades > 90:" , grades[grades > 90])

print()

new_student = np.array([[75, 80, 85]])

updated_array = np.vstack((grades , new_student))

print("Updated Grades:" , updated_array)

print()

updated_student_average = np.mean(updated_array , axis = 1)

print("New Student Average:" , updated_student_average)

print()

print("New Shape:" , updated_array.shape)
