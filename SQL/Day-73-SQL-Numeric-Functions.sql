SELECT name, salary, salary * 12 AS annual_salary
FROM employees;

SELECT name, salary, salary + 1000
FROM employees;

SELECT name, ABS(salary - 6000)
FROM employees;

SELECT ROUND(AVG(salary) , 2), CEIL(AVG(salary)), FLOOR(AVG(salary))
FROM employees;

select name, salary, POWER(salary, 2) AS salary_squared
FROM employees;

SELECT *
FROM employees
WHERE salary * 12 > 80000;

SELECT department, ROUND(AVG(salary), 2) AS average_salary, CEIL(AVG(salary))
FROM employees
GROUP BY department;

SELECT name, salary, salary * 12 AS annual_salary, ABS(salary - 7000) AS difference_from_7000
FROM employees;

SELECT department, COUNT(*) AS employee_count, SUM(salary * 12) AS total_annual_salary, AVG(salary) AS average_salary, ROUND(AVG(salary), 2) AS rounded_average_salary
FROM employees
WHERE salary > 4000
GROUP BY department
HAVING COUNT(*) >= 2
ORDER BY ROUND(AVG(salary), 2) DESC;
