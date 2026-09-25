SELECT *
FROM employees_join
WHERE department_id IS NULL;

SELECT *
FROM employees_join
WHERE department_id IS NOT NULL;

SELECT e.name, COALESCE(d.department_name, 'Unknown Department') AS department_name
FROM employees_join e
LEFT JOIN departments d
ON e.department_id = d.id;

SELECT
    name,
    salary,
    CASE
        WHEN salary >= 7500 THEN 'High'
        WHEN salary >= 6500 THEN 'Medium'
        ELSE 'Low'
    END AS salary_level
FROM employees_join;

SELECT *,
    CASE
        WHEN department_name = 'IT' THEN 'Technology'
        WHEN department_name = 'HR' THEN 'Human Resources'
        WHEN department_name = 'Finance' THEN 'Financial'
        ELSE 'Other'
    END AS Department_Category
FROM departments;

SELECT
    name,
    salary,
    CASE
        WHEN salary >= 7000 THEN 'High Salary'
        ELSE 'Normal Salary'
    END AS salary_level
FROM employees_join;

SELECT
    e.name,
    d.department_name,
    CASE
        WHEN d.department_name IS NULL THEN 'Unassigned'
        ELSE 'Assigned'
    END AS department_status
FROM employees_join e
LEFT JOIN departments d
ON e.department_id = d.id;

SELECT e.name, COALESCE(d.department_name, 'Unknown Department') AS department_name,
COALESCE(d.location, 'Unknown Location') AS location_name
FROM employees_join e
LEFT JOIN departments d
ON e.department_id = d.id;

SELECT
    e.name,
    e.salary,
    CASE
        WHEN e.salary >= 7000 AND d.department_name = 'IT' THEN 'High IT Salary'
        WHEN e.salary >= 7000 THEN 'High Salary'
        ELSE 'Other'
    END AS salary_category
FROM employees_join e
LEFT JOIN departments d
ON e.department_id = d.id;

SELECT
    e.name AS "Employee Name",
    d.department_name AS "Department Name",
    e.salary AS "Salary",
    CASE
        WHEN e.salary >= 7500 THEN 'High'
        WHEN e.salary >= 6500 THEN 'Medium'
        ELSE 'Low'
    END AS "Salary Category",
    CASE
        WHEN d.department_name IS NULL THEN 'Unassigned'
        ELSE 'Assigned'
    END AS "Department Status"
FROM employees_join e
LEFT JOIN departments d
    ON e.department_id = d.id;
