SELECT
    name,
    department_id,
    salary,
    AVG(salary) OVER() AS company_avg_salary
FROM employees_join;

SELECT
    name,
    department_id,
    salary,
    AVG(salary) OVER(
        PARTITION BY department_id
    ) AS department_avg_salary
FROM employees_join;

SELECT
    name,
    salary,
    ROW_NUMBER() OVER(
        ORDER BY salary DESC
    ) AS row_num
FROM employees_join;

SELECT
    name,
    department_id,
    salary,
    ROW_NUMBER() OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS department_rank
FROM employees_join;

SELECT
    name,
    salary,
    RANK() OVER(
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees_join;

SELECT
    name,
    salary,
    DENSE_RANK() OVER(
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees_join;

SELECT
    name,
    department_id,
    salary,
    RANK() OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS department_rank
FROM employees_join;

SELECT
    name,
    salary,
    LAG(salary) OVER(
        ORDER BY salary
    ) AS previous_salary
FROM employees_join;

SELECT
    name,
    salary,
    LEAD(salary) OVER(
        ORDER BY salary
    ) AS next_salary
FROM employees_join;

WITH ranked_employees AS (
    SELECT
        e.name,
        e.department_id,
        e.salary,
        RANK() OVER (
            PARTITION BY e.department_id
            ORDER BY e.salary DESC
        ) AS department_rank
    FROM employees_join e
)
SELECT
    ranked_employees.name,
    d.department_name,
    ranked_employees.salary,
    ranked_employees.department_rank
FROM ranked_employees
JOIN departments d
    ON ranked_employees.department_id = d.id
WHERE ranked_employees.department_rank = 1
ORDER BY ranked_employees.salary DESC;
