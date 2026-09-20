SELECT COUNT(*)
FROM employees;

SELECT SUM(salary)
FROM employees;

SELECT ROUND(AVG(salary) , 2)
FROM employees;

SELECT MIN(salary)
FROM employees;

SELECT MAX(salary)
FROM employees;

SELECT COUNT(*)
FROM employees
WHERE department = 'IT';

SELECT SUM(salary)
FROM employees
WHERE department = 'IT';

SELECT ROUND(AVG(salary) , 2)
FROM employees
WHERE department = 'HR';

SELECT
    COUNT(*) AS employee_count,
    SUM(Salary) AS total_salary,
    ROUND(AVG(Salary) , 2) AS average_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM employees;

SELECT COUNT(*)
FROM employees
WHERE Salary > 6000;
