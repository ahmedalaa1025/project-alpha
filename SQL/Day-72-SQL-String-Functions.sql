SELECT UPPER(name)
FROM employees;

SELECT LOWER(name)
FROM employees;

SELECT name, LENGTH(name)
FROM employees;

SELECT name, department, UPPER(name) AS upper_name, LOWER(department) AS lower_department
FROM employees;

SELECT name || '-' || department AS name_department
FROM employees;

SELECT UPPER(name) || '-' || UPPER(department)
FROM employees;

SELECT *
FROM employees
WHERE LENGTH(name) > 5;

SELECT *
FROM employees
WHERE UPPER(department) = 'IT';

SELECT name, LENGTH(name) AS name_length
FROM employees
ORDER BY name_length DESC;

SELECT UPPER(department), COUNT(*) AS employee_count, ROUND(AVG(salary) , 2) AS avg_salary
FROM employees
WHERE salary > 4000
GROUP BY department
HAVING COUNT(*) >= 2
ORDER BY ROUND(AVG(salary), 2) DESC;
