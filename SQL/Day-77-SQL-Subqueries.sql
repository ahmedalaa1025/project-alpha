SELECT name, salary
FROM employees_join
WHERE salary > (
  SELECT AVG(salary)
  FROM employees_join
);

SELECT name, salary
FROM employees_join
WHERE salary = (
  SELECT MAX(salary)
  FROM employees_join
);

SELECT name, salary
FROM employees_join
WHERE salary = (
  SELECT MIN(salary)
  FROM employees_join
);

SELECT name, department_id
FROM employees_join
WHERE department_id IN (
  SELECT id
  FROM departments
  WHERE location = 'Cairo'
);

SELECT name, salary
FROM employees_join
WHERE salary < (
  SELECT AVG(salary)
  FROM employees_join
);

SELECT *
FROM (
  SELECT department_id, AVG(salary) AS avg_salary
  FROM employees_join
  GROUP BY department_id
) AS dept_avg;


SELECT *
FROM (
  SELECT department_id, AVG(salary) AS avg_salary
  FROM employees_join
  GROUP BY department_id
) AS dept_avg
WHERE avg_salary > 6500;

SELECT e.name, e.salary, e.department_id
FROM employees_join e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees_join e2
    WHERE e2.department_id = e.department_id
);

SELECT name, salary
FROM employees_join
WHERE department_id = 10 
AND salary = 
(
  SELECT MAX(salary)
  FROM employees_join
  WHERE department_id = 10
);

SELECT e.name, e.salary, d.department_name
FROM employees_join e
JOIN departments d 
ON e.department_id = d.id
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees_join e2
    WHERE e2.department_id = e.department_id
);
