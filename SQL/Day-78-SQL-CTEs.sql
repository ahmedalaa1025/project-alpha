WITH high_salary AS (
    SELECT name, salary
    FROM employees_join
)
SELECT *
FROM high_salary
WHERE salary > 7000;

WITH department_stats AS (
    SELECT department_id, COUNT(*) AS employee_count, AVG(salary) AS average_salary, MAX(salary) AS max_salary 
    FROM employees_join
    GROUP BY department_id
)
SELECT *
FROM department_stats;

WITH dept_avg AS (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees_join
    GROUP BY department_id
)
SELECT *
FROM dept_avg
WHERE avg_salary > 6500;

WITH department_max_salary AS (
    SELECT
        name, department_id, salary
    FROM employees_join
    WHERE salary > 6500
)
SELECT
    department_max_salary.name,
    d.department_name,
    department_max_salary.salary
FROM department_max_salary
JOIN departments d
ON department_max_salary.department_id = d.id;

WITH dept_employee_count AS (
    SELECT
       COUNT(*) AS employee_count, department_id
    FROM employees_join
    GROUP BY department_id
    HAVING COUNT(*) > 1
)
SELECT
    d.department_name,
    dept_employee_count.employee_count
FROM dept_employee_count
JOIN departments d
ON dept_employee_count.department_id = d.id;

WITH department_stats AS (
    SELECT
      department_id, COUNT(*) AS employee_count, AVG(salary) AS average_salary
    FROM employees_join
    GROUP BY department_id
)
SELECT
    d.department_name,
    department_stats.average_salary,
    department_stats.employee_count
FROM department_stats
JOIN departments d
ON department_stats.department_id = d.id;

WITH employee_data AS (
    SELECT
        department_id,
        salary
    FROM employees_join
),
department_avg AS (
    SELECT
        department_id,
        AVG(salary) AS avg_salary
    FROM employee_data
    GROUP BY department_id
)
SELECT *
FROM department_avg;

WITH dept_stats AS (
    SELECT
        department_id,
        COUNT(*) AS employee_count, AVG(salary) AS avg_salary
    FROM employees_join
    GROUP BY department_id
),
filter_dept AS (
    SELECT
        department_id,
        employee_count,
        avg_salary
    FROM dept_stats
    WHERE employee_count > 1
)
SELECT *
FROM filter_dept;

WITH dept_salary_stats AS (
    SELECT
        department_id,
        SUM(salary) AS total_salary,
        AVG(salary) AS avg_salary
    FROM employees_join
    GROUP BY department_id
)
SELECT
    d.department_name,
    d.location,
    dept_salary_stats.total_salary,
    dept_salary_stats.avg_salary
FROM dept_salary_stats
JOIN departments d
    ON dept_salary_stats.department_id = d.id
ORDER BY dept_salary_stats.avg_salary DESC;

WITH dept_stats AS (
    SELECT
        department_id,
        COUNT(*) AS employee_count,
        AVG(salary) AS avg_salary,
        MAX(salary) AS max_salary
    FROM employees_join
    GROUP BY department_id
    HAVING COUNT(*) > 1
       AND AVG(salary) > 6500
)
SELECT
    d.department_name,
    d.location,
    dept_stats.employee_count,
    dept_stats.avg_salary,
    dept_stats.max_salary
FROM dept_stats
JOIN departments d
    ON dept_stats.department_id = d.id
ORDER BY dept_stats.avg_salary DESC;
