SELECT
    name,
    hire_date,
    EXTRACT(YEAR FROM hire_date) AS year,
    EXTRACT(MONTH FROM hire_date) AS month,
    EXTRACT(DAY FROM hire_date) AS day
FROM employees_dates;

SELECT
    name,
    hire_date
FROM employees_dates
WHERE hire_date > '2021-01-01';

SELECT
    name,
    hire_date
FROM employees_dates
WHERE hire_date BETWEEN '2021-01-01' AND '2022-12-31';

SELECT
    name, hire_date,
    AGE(CURRENT_DATE, hire_date) AS employment_period
FROM employees_dates;

SELECT
    EXTRACT(YEAR FROM hire_date) AS hire_year,
    COUNT(*) AS employee_count
FROM employees_dates
GROUP BY EXTRACT(YEAR FROM hire_date)
ORDER BY hire_year;

SELECT
    EXTRACT(MONTH FROM hire_date) AS hire_month,
    COUNT(*) AS employee_count
FROM employees_dates
GROUP BY EXTRACT(MONTH FROM hire_date)
ORDER BY hire_month;

SELECT
    EXTRACT(YEAR FROM hire_date) AS hire_year,
    EXTRACT(MONTH FROM hire_date) AS hire_month,
    COUNT(*) AS employee_count
FROM employees_dates
GROUP BY
    EXTRACT(YEAR FROM hire_date),
    EXTRACT(MONTH FROM hire_date)
ORDER BY
    hire_year,
    hire_month;

    SELECT
    COUNT(*) AS employee_count,
    DATE_TRUNC('month', hire_date) AS hire_month
FROM employees_dates
GROUP BY DATE_TRUNC('month', hire_date);

SELECT
    d.department_name,
    EXTRACT(YEAR FROM e.hire_date) AS hire_year,
    COUNT(*) AS employee_count
FROM employees_dates e
JOIN departments d
ON e.department_id = d.id
GROUP BY
    d.department_name,
    EXTRACT(YEAR FROM e.hire_date)
HAVING COUNT(*) > 0
ORDER BY
    hire_year,
    d.department_name;

    WITH hiring_per_year AS (
    SELECT
        d.department_name,
        EXTRACT(YEAR FROM e.hire_date) AS hire_year,
        COUNT(*) AS employee_count
    FROM employees_dates e
    JOIN departments d
        ON e.department_id = d.id
    GROUP BY
        d.department_name,
        EXTRACT(YEAR FROM e.hire_date)
        HAVING COUNT(*) > 1
)
SELECT
    department_name,
    hire_year,
    employee_count
FROM hiring_per_year
ORDER BY
    hire_year,
    department_name;
