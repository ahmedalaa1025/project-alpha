SELECT e.name, d.department_name
FROM employees_join e
INNER JOIN departments d 
ON e.department_id = d.id;

SELECT e.name, d.department_name, e.salary
FROM employees_join e
LEFT JOIN departments d 
ON e.department_id = d.id;

SELECT e.name, d.department_name, d.location
FROM employees_join e
RIGHT JOIN departments d 
ON e.department_id = d.id;

SELECT e.name, d.department_name
FROM employees_join e
FULL OUTER JOIN departments d 
ON e.department_id = d.id;

SELECT e.name, d.department_name
FROM employees_join e
LEFT JOIN departments d
ON e.department_id = d.id
WHERE d.id IS NULL;

SELECT e.name, d.department_name
FROM employees_join e
INNER JOIN departments d
ON e.department_id = d.id
WHERE d.department_name = 'IT';

SELECT e.name, d.department_name, e.salary
FROM employees_join e
INNER JOIN departments d
ON e.department_id = d.id
ORDER BY e.salary DESC;

SELECT e.name, d.department_name, d.location, e.salary
FROM employees_join e
INNER JOIN departments d
ON e.department_id = d.id
WHERE e.salary > 6500;

SELECT COUNT(e.id), d.department_name
FROM employees_join e
LEFT JOIN departments d
ON e.department_id = d.id
GROUP BY d.department_name;
