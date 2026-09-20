SELECT *
FROM employees
ORDER BY salary ASC;

SELECT *
FROM employees
ORDER BY salary DESC;

SELECT *
FROM employees
ORDER BY department ASC , salary DESC;

SELECT *
FROM employees
WHERE department = 'IT'
ORDER BY salary DESC;

SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;

SELECT *
FROM employees
WHERE department = 'HR'
ORDER BY salary DESC
LIMIT 2;

SELECT *
FROM employees
LIMIT 4;
