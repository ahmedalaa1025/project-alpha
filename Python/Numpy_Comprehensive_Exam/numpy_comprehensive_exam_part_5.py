# Question (5)

import numpy as np

grades = np.array([
    [85, 90, 88, 92],
    [70, 65, 68, 72],
    [95, 98, 94, 97],
    [55, 60, 58, 62],
    [80, 82, 84, 86],
    [90, 91, 89, 93]
])

print("===== Student Grade Analysis =====")

print()

print("Shape:" , grades.shape)

print("Size:" , grades.size)

print("Dimensions:" , grades.ndim)

print()

total_grades_per_student = np.sum(grades , axis = 1)

average_grades_per_student = np.mean(grades , axis = 1)

print("Student Total:" , total_grades_per_student)

print()

print("Student Average:" , average_grades_per_student)

print()

status = np.where(grades >= 70 , "Pass" , "Fail")

print("Student Status:" , status)

print()

average_grades_per_course = np.mean(grades , axis = 0)

print("Subject Average:" , average_grades_per_course)

print()

high_mark_per_subject = np.max(grades , axis = 0)

print("Highest Grade Per Subject:" , high_mark_per_subject)

print()

marks_higher_90 = grades[grades > 90]

print("Grades > 90:" , marks_higher_90)

print()

new_student = np.array([[78, 81, 79, 83]])

updated_grades = np.vstack((grades , new_student))

print("Updated Grades:" , updated_grades)

print()

vertical_updated_grades = np.array_split(updated_grades , 2)

print("Upper Half:" , vertical_updated_grades[0])

print()

print("Lower Half:" , vertical_updated_grades[1])

unique_grades , counts = np.unique(updated_grades , return_counts = True)

print("Unique Values:" , unique_grades)

print()

print("Counts:" , counts)

print()

maximum_grade = np.max(updated_grades)

print("Maximum Grade:" , maximum_grade)

print()

maximum_grade_index = np.argmax(updated_grades)

print("Argmax:" , maximum_grade_index)

print()

print("Any == 100:" , np.any(updated_grades == 100))

print()

print("All >= 55:" , np.all(updated_grades >= 55))

print()

reshaped = np.reshape(updated_grades , (4 , 7))

print("Reshaped:" , reshaped)
