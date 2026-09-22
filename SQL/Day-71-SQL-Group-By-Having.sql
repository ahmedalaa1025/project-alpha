SELECT department, COUNT(*)
FROM employees
GROUP BY department;

SELECT department, SUM(salary)
FROM employees
GROUP BY department;

SELECT department, ROUND(AVG(salary) , 2)
FROM employees
GROUP BY department;

SELECT department, MIN(salary), MAX(salary)
FROM employees
GROUP BY department;

SELECT department, COUNT(*) AS Employee_Count, SUM(salary) AS Total_Salary, ROUND(AVG(salary), 2) AS Average_Salary
FROM employees
GROUP BY department;

SELECT department, COUNT(*)
FROM employees
WHERE salary > 5000
GROUP BY department;

SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;

SELECT department, ROUND(AVG(salary), 2)
FROM employees
GROUP BY department
HAVING ROUND(AVG(salary), 2) > 6000;

SELECT department, SUM(salary) AS Total_Salary
FROM employees
GROUP BY department
HAVING SUM(salary) > 20000;

SELECT department, COUNT(*), ROUND(AVG(salary), 2)
FROM employees
WHERE salary > 4000
GROUP BY department
HAVING COUNT(*) >= 2
ORDER BY ROUND(AVG(salary), 2) DESC;
