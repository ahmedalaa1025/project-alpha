import numpy as np

grades = np.array([
    [80, 75, 90, 85],  
    [60, 70, 65, 75],  
    [95, 88, 92, 90]   
])

result0 = np.sum(grades, axis = 1)
print(result0)

result1 = np.mean(grades, axis = 1)
print(result1)

result2 = np.max(grades, axis = 0)
print(result2)

new_student = np.array([
    [88, 92, 85, 90]
])

result3 = np.vstack((grades, new_student))
print(result3)

result4 = np.mean(result3, axis = 1)
print(result4)

result5 = np.where(result4 >= 70, "Pass", "Fail")
print(result5)