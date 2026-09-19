SELECT *
FROM employees
WHERE department = 'IT';

SELECT *
FROM employees
WHERE salary > 6500;

SELECT *
FROM employees
WHERE department = 'IT' AND experience > 2;

SELECT *
FROM employees
WHERE department = 'HR' OR department = 'Finance';

SELECT *
FROM employees
WHERE NOT department = 'HR';

SELECT *
FROM employees
WHERE department IN ('IT', 'HR');

SELECT *
FROM employees
WHERE salary BETWEEN 6000 AND 7500;

SELECT *
FROM employees
WHERE name LIKE 'A%';

SELECT *
FROM employees
WHERE name LIKE '%a%';
