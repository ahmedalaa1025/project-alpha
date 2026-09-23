SELECT UPPER(name), LOWER(department), salary, salary * 12 AS annual_salary
FROM employees;

SELECT name, salary, salary * 12 AS annual_salary, ABS(salary - 7000) AS salary_difference
FROM employees;

SELECT *
FROM employees
WHERE LENGTH(name) > 5 AND salary * 12 > 80000;

SELECT UPPER(name) || ' | ' || UPPER(department) || ' | ' || salary
FROM employees;

SELECT UPPER(department) AS department, COUNT(*) AS employee_count, ROUND(AVG(salary) , 2) AS average_salary, MAX(salary) AS maximum_salary
FROM employees
GROUP BY department;

SELECT department, COUNT(*), ROUND(AVG(salary) , 2) AS average_salary
FROM employees
WHERE salary > 4000
GROUP BY department
HAVING COUNT(*) >= 2 AND AVG(salary) > 6000;

SELECT name, salary * 12 AS annual_salary, ABS(salary - 7000) AS salary_difference
FROM employees
ORDER BY salary_difference ASC;

SELECT department, COUNT(*) AS employee_count, SUM(salary * 12) AS total_annual_salary, ROUND(AVG(salary) , 2) AS average_salary
FROM employees
WHERE salary > 4000
GROUP BY department
HAVING COUNT(*) >= 2
ORDER BY total_annual_salary DESC;

SELECT UPPER(department), COUNT(*) AS employee_count, ROUND(AVG(salary) , 2) AS average_salary, SUM(salary * 12) AS total_annual_salary, CEIL(AVG(salary)) AS rounded_up_average, FLOOR(AVG(salary)) AS rounded_down_average
FROM employees
WHERE salary > 4000
GROUP BY department
HAVING COUNT(*) >= 2 AND AVG(salary) > 6000
ORDER BY average_salary DESC;
