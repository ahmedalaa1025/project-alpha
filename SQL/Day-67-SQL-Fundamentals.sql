-- Query 1: Display employee information and annual salary
SELECT Name, Department, Salary AS Monthly_Salary, Salary * 12 AS Annual_Salary
FROM Employees;

-- Query 2: Display all different departments
SELECT DISTINCT Department
FROM Employees;