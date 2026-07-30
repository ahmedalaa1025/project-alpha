# Final NumPy Project

import numpy as np

grades = np.array([
    [85, 90, 88, 92, 80],
    [70, 65, 68, 72, 75],
    [95, 98, 94, 97, 99],
    [55, 60, 58, 62, 57],
    [80, 82, 84, 86, 88],
    [90, 91, 89, 93, 95],
    [76, 79, 81, 77, 80],
    [60, 58, 55, 62, 64]
])

print("===== Student Performance Analysis System =====")

print()

print("Shape:" , grades.shape)

print("Size:" , grades.size)

print("Dimensions:" , grades.ndim)

print()

total_student_marks = np.sum(grades , axis = 1)

average_student_marks = np.mean(grades , axis = 1)

print("Total Marks:" , total_student_marks)

print()

print("Average Marks:" , average_student_marks)

print()

higher_student_mark = np.max(grades , axis = 1)

lower_student_mark = np.min(grades , axis = 1)

print("Higher Mark:" , higher_student_mark)

print()

print("Lower Mark:" , lower_student_mark)

print()

total_subject_marks = np.sum(grades , axis = 0)

average_subject_marks = np.mean(grades , axis = 0)

higher_subject_mark = np.max(grades , axis = 0)

lower_subject_mark = np.min(grades , axis = 0)

print("Total Subject Marks:" , total_subject_marks)

print()

print("Average Subject Marks:" , average_subject_marks)

print()

print("Higher Subject Mark:" , higher_subject_mark)

print()

print("Lower Mark:" , lower_subject_mark)

print()

status = np.where(average_student_marks >= 70 , "Pass" , "Fail")

print("Student Status:" , status)

print()

print("Grades > 90:" , grades[grades > 90])

print()

print("Grades < 60:" , grades[grades < 60])

print()

new_student = np.array([[88, 90, 85, 87, 89]])

updated_grades = np.vstack((grades , new_student))

print("Updated Grades:" , updated_grades)

print()

new_array = np.array_split(updated_grades , 3)

print(new_array[0])
print(new_array[1])
print(new_array[2])

print()

unique_values , counts = np.unique(updated_grades , return_counts = True)

print("Unique Grades:" , unique_values)

print()

print("Counts:" , counts)

print()

maximum_grade = np.max(updated_grades)

maximum_grade_index = np.argmax(updated_grades)

print("Maximum Grade:" , maximum_grade)

print()

print("Argmax:" , maximum_grade_index)

print()

print("Any == 100:" , np.any(updated_grades == 100))

print()

print("All >= 55:" , np.all(updated_grades >= 55))

print()

total = np.sum(updated_grades , axis = 1 , keepdims = True)

normalized = updated_grades / total

print("Normalized:" , normalized)

print()

reshape = np.reshape(normalized , (9 , 5))

print("Reshaped:" , reshape)

print()

reshape_another_way = np.reshape(normalized , (5 , 9))

print("Reshaped Another Way:" , reshape_another_way)
