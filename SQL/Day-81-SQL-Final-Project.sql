SELECT 
    (SELECT COUNT(*) FROM employees)              AS total_employees,
    (SELECT COUNT(*) FROM departments)            AS total_departments,
    (SELECT COUNT(*) FROM projects)               AS total_projects,
    (SELECT COUNT(*) FROM employee_projects)      AS total_assignments,
    (SELECT MIN(salary) FROM employees)           AS min_salary,
    (SELECT MAX(salary) FROM employees)           AS max_salary,
    (SELECT ROUND(AVG(salary), 2) FROM employees) AS avg_salary,
    (SELECT MIN(hire_date) FROM employees)        AS oldest_hire_date,
    (SELECT MAX(hire_date) FROM employees)        AS newest_hire_date;
SELECT 
    (SELECT COUNT(*) FROM employees WHERE department_id IS NULL)                     AS employees_without_dept,
    (SELECT COUNT(*) FROM projects WHERE department_id IS NULL)                      AS projects_without_dept,
    (SELECT COUNT(*) FROM employees e
        LEFT JOIN employee_projects ep ON e.employee_id = ep.employee_id
        WHERE ep.project_id IS NULL)                                                 AS employees_without_project,
    (SELECT COUNT(*) FROM projects p
        LEFT JOIN employee_projects ep ON p.project_id = ep.project_id
        WHERE ep.employee_id IS NULL)                                                AS projects_without_employee;

SELECT 
    'INNER JOIN (employees + departments)' AS join_type,
    COUNT(*) AS row_count
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id

UNION ALL

SELECT 
    'LEFT JOIN (employees + departments)',
    COUNT(*)
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id

UNION ALL

SELECT 
    'RIGHT JOIN (employees + departments)',
    COUNT(*)
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.department_id

UNION ALL

SELECT 
    'FULL OUTER JOIN (employees + departments)',
    COUNT(*)
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.department_id

UNION ALL

SELECT 
    'INNER JOIN (employees + employee_projects + projects)',
    COUNT(*)
FROM employees e
INNER JOIN employee_projects ep ON e.employee_id = ep.employee_id
INNER JOIN projects p ON ep.project_id = p.project_id

UNION ALL

SELECT 
    'LEFT JOIN (employees + employee_projects + projects)',
    COUNT(*)
FROM employees e
LEFT JOIN employee_projects ep ON e.employee_id = ep.employee_id
LEFT JOIN projects p ON ep.project_id = p.project_id

UNION ALL

SELECT 
    'RIGHT JOIN (employees + employee_projects + projects)',
    COUNT(*)
FROM employees e
RIGHT JOIN employee_projects ep ON e.employee_id = ep.employee_id
RIGHT JOIN projects p ON ep.project_id = p.project_id

UNION ALL

SELECT 
    'FULL OUTER JOIN (employees + employee_projects + projects)',
    COUNT(*)
FROM employees e
FULL OUTER JOIN employee_projects ep ON e.employee_id = ep.employee_id
FULL OUTER JOIN projects p ON ep.project_id = p.project_id;

SELECT 
    d.department_name,
    COUNT(e.employee_id)          AS employee_count,
    ROUND(AVG(e.salary), 2)       AS avg_salary,
    SUM(e.salary)                 AS total_salaries,
    MAX(e.salary)                 AS max_salary,
    MIN(e.salary)                 AS min_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > 6000
GROUP BY d.department_name
HAVING COUNT(e.employee_id) >= 1
ORDER BY total_salaries DESC;

SELECT 
    e.name,
    d.department_name,
    e.salary,
    CASE 
        WHEN e.salary >= 8000 THEN 'High'
        WHEN e.salary >= 6500 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category,
    CASE 
        WHEN d.department_name IN ('IT', 'Finance', 'Operations') THEN 'Technical / Core'
        WHEN d.department_name IN ('HR', 'Marketing')             THEN 'Support / Creative'
        WHEN d.department_name IN ('Sales')                       THEN 'Revenue'
        ELSE 'Unassigned'
    END AS department_category
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
ORDER BY e.salary DESC;

SELECT 
    'Q1: Above Company Avg' AS question,
    e.name                  AS employee_name,
    d.department_name,
    e.salary
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > (SELECT AVG(salary) FROM employees)          

UNION ALL

SELECT 
    'Q2: Above Dept Avg',
    e.name,
    d.department_name,
    e.salary
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > (                                            
        SELECT AVG(e2.salary)
        FROM employees e2
        WHERE e2.department_id = e.department_id
      )

UNION ALL

SELECT 
    'Q3: Top Earner',
    e.name,
    d.department_name,
    e.salary
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
WHERE e.salary = (SELECT MAX(salary) FROM employees)          

UNION ALL

SELECT 
    'Q4: Depts in Cairo',
    d.department_name,
    d.location,
    NULL
FROM (                                                        
        SELECT department_id, department_name, location
        FROM departments
        WHERE location = 'Cairo'
     ) d
ORDER BY question, salary DESC NULLS LAST;

WITH dept_stats AS (
    -- Department Statistics
    SELECT 
        d.department_id,
        d.department_name,
        d.location,
        COUNT(e.employee_id)     AS employee_count,
        COALESCE(SUM(e.salary),0) AS total_salaries,
        ROUND(AVG(e.salary), 2)  AS avg_salary
    FROM departments d
    LEFT JOIN employees e ON d.department_id = e.department_id
    GROUP BY d.department_id, d.department_name, d.location
),
emp_stats AS (
   
    SELECT 
        e.employee_id,
        e.name,
        e.department_id,
        e.salary,
        COUNT(ep.project_id)   AS project_count,
        COALESCE(SUM(ep.hours_worked),0) AS total_hours
    FROM employees e
    LEFT JOIN employee_projects ep ON e.employee_id = ep.employee_id
    GROUP BY e.employee_id, e.name, e.department_id, e.salary
),
project_stats AS (
   
    SELECT 
        p.project_id,
        p.project_name,
        p.department_id,
        p.budget,
        COUNT(ep.employee_id) AS assigned_employees,
        COALESCE(SUM(ep.hours_worked),0) AS total_hours
    FROM projects p
    LEFT JOIN employee_projects ep ON p.project_id = ep.project_id
    GROUP BY p.project_id, p.project_name, p.department_id, p.budget
),
salary_stats AS (
  
    SELECT 
        MIN(salary)           AS min_salary,
        MAX(salary)           AS max_salary,
        ROUND(AVG(salary),2)  AS avg_salary,
        SUM(salary)           AS total_salaries
    FROM employees
)
SELECT 
    ds.department_name,
    ds.location,
    ds.employee_count,
    ds.total_salaries,
    ds.avg_salary,
    ss.min_salary   AS company_min,
    ss.max_salary   AS company_max,
    ss.avg_salary   AS company_avg
FROM dept_stats ds
CROSS JOIN salary_stats ss
ORDER BY ds.total_salaries DESC NULLS LAST;

SELECT 
    e.employee_id,
    e.name,
    d.department_name,
    e.salary,

    -- 1) ROW_NUMBER: unique sequence across all employees by salary
    ROW_NUMBER() OVER (ORDER BY e.salary DESC) AS row_num_global,

    -- 2) RANK: rank by salary (ties share rank, gaps after)
    RANK()       OVER (ORDER BY e.salary DESC) AS rank_global,

    -- 3) DENSE_RANK: rank by salary (ties share rank, no gaps)
    DENSE_RANK() OVER (ORDER BY e.salary DESC) AS dense_rank_global,

    -- 4) ROW_NUMBER inside department
    ROW_NUMBER() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS row_num_in_dept,

    -- 5) RANK inside department
    RANK()       OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS rank_in_dept,

    -- 6) LAG: previous salary (higher, since DESC) in same department
    LAG(e.salary)  OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS prev_salary,

    -- 7) LEAD: next salary in same department
    LEAD(e.salary) OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS next_salary,

    -- 8) Difference vs previous
    e.salary - LAG(e.salary)  OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS diff_from_prev,

    -- 9) Difference vs next
    e.salary - LEAD(e.salary) OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS diff_from_next

FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
ORDER BY e.salary DESC;

WITH hire_by_year AS (
    SELECT 
        EXTRACT(YEAR FROM hire_date)::int AS hire_year,
        COUNT(*)                          AS employees_hired
    FROM employees
    GROUP BY EXTRACT(YEAR FROM hire_date)
),
hire_by_month AS (
    SELECT 
        DATE_TRUNC('month', hire_date)::date AS hire_month,
        COUNT(*)                              AS employees_hired
    FROM employees
    GROUP BY DATE_TRUNC('month', hire_date)
),
oldest_newest AS (
    SELECT 
        MIN(hire_date) AS oldest_hire,
        MAX(hire_date) AS newest_hire
    FROM employees
),
emp_tenure AS (
    SELECT 
        e.name,
        e.hire_date,
        AGE(CURRENT_DATE, e.hire_date) AS tenure
    FROM employees e
),
proj_by_year AS (
    SELECT 
        EXTRACT(YEAR FROM start_date)::int AS start_year,
        COUNT(*)                            AS projects_started,
        SUM(budget)                         AS total_budget
    FROM projects
    GROUP BY EXTRACT(YEAR FROM start_date)
),
proj_duration AS (
    SELECT 
        p.project_name,
        p.start_date,
        p.end_date,
        AGE(p.end_date, p.start_date) AS duration
    FROM projects p
)
SELECT 'HIRE_BY_YEAR' AS section,
       hire_year::text AS label,
       employees_hired::text AS value
FROM hire_by_year

UNION ALL

SELECT 'HIRE_BY_MONTH',
       hire_month::text,
       employees_hired::text
FROM hire_by_month

UNION ALL

SELECT 'OLDEST_NEWEST',
       'Oldest: ' || oldest_hire::text || ' | Newest: ' || newest_hire::text,
       NULL
FROM oldest_newest

UNION ALL

SELECT 'EMP_TENURE',
       name || ' (hired ' || hire_date::text || ')',
       tenure::text
FROM emp_tenure

UNION ALL

SELECT 'PROJECTS_BY_YEAR',
       start_year::text,
       projects_started::text || ' projects, budget ' || total_budget::text
FROM proj_by_year

UNION ALL

SELECT 'PROJECT_DURATION',
       project_name,
       duration::text
FROM proj_duration

ORDER BY section, label;

WITH project_details AS (
    SELECT 
        p.project_id,
        p.project_name,
        p.department_id,
        d.department_name,
        p.budget,
        COUNT(ep.employee_id)            AS employee_count,
        COALESCE(SUM(ep.hours_worked),0) AS total_hours
    FROM projects p
    LEFT JOIN departments d        ON p.department_id = d.department_id
    LEFT JOIN employee_projects ep ON p.project_id = ep.project_id
    GROUP BY p.project_id, p.project_name, p.department_id, d.department_name, p.budget
)
SELECT 'TOTAL_BUDGET'       AS section, 'All Projects'              AS label, SUM(budget)::text        AS value FROM project_details
UNION ALL
SELECT 'AVG_BUDGET',        'All Projects',                                ROUND(AVG(budget),2)::text FROM project_details
UNION ALL
SELECT 'HIGHEST_BUDGET',    project_name,                                  budget::text               FROM project_details WHERE budget = (SELECT MAX(budget) FROM project_details)
UNION ALL
SELECT 'EMP_PER_PROJECT',   project_name,                                  employee_count::text       FROM project_details
UNION ALL
SELECT 'HOURS_PER_PROJECT', project_name,                                  total_hours::text          FROM project_details
UNION ALL
SELECT 'DEPT_BUDGET',       COALESCE(department_name, 'Unassigned'),       SUM(budget)::text          FROM project_details GROUP BY department_name
UNION ALL
SELECT 'TOP_WORKLOAD',      project_name,                                  total_hours::text
FROM (
    SELECT project_name, total_hours
    FROM project_details
    ORDER BY total_hours DESC
    LIMIT 1
) top1
ORDER BY section, label;

-- ============================================================
-- Q1: Department with the highest average salary
-- ============================================================
SELECT 'Q1: Highest Avg Salary Dept' AS question,
       d.department_name            AS answer,
       ROUND(AVG(e.salary), 2)::text AS detail
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY AVG(e.salary) DESC
LIMIT 1;

-- ============================================================
-- Q2: Highest-paid employee in each department
-- ============================================================
SELECT 'Q2: Highest-Paid per Dept' AS question,
       d.department_name           AS answer,
       e.name || ' (' || e.salary || ')' AS detail
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary = (
    SELECT MAX(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
)
ORDER BY e.salary DESC;

-- ============================================================
-- Q3: Department with the largest number of employees
-- ============================================================
SELECT 'Q3: Largest Dept by Headcount' AS question,
       d.department_name               AS answer,
       COUNT(e.employee_id)::text      AS detail
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY COUNT(e.employee_id) DESC
LIMIT 1;

-- ============================================================
-- Q4: Employees earning more than their department average
-- ============================================================
SELECT 'Q4: Above Dept Avg'    AS question,
       e.name                  AS answer,
       d.department_name || ' — ' || e.salary AS detail
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
)
ORDER BY e.salary DESC;

-- ============================================================
-- Q5: Projects with the highest total hours worked
-- ============================================================
SELECT 'Q5: Top Projects by Hours' AS question,
       p.project_name              AS answer,
       SUM(ep.hours_worked)::text  AS detail
FROM projects p
JOIN employee_projects ep ON p.project_id = ep.project_id
GROUP BY p.project_name
ORDER BY SUM(ep.hours_worked) DESC;

-- ============================================================
-- Q6: Employees working on multiple projects
-- ============================================================
SELECT 'Q6: Multi-Project Employees' AS question,
       e.name                        AS answer,
       COUNT(ep.project_id)::text    AS detail
FROM employees e
JOIN employee_projects ep ON e.employee_id = ep.employee_id
GROUP BY e.employee_id, e.name
HAVING COUNT(ep.project_id) > 1
ORDER BY COUNT(ep.project_id) DESC;

-- ============================================================
-- Q7: Year with the highest number of new employees
-- ============================================================
SELECT 'Q7: Best Hiring Year'           AS question,
       EXTRACT(YEAR FROM hire_date)::text AS answer,
       COUNT(*)::text                     AS detail
FROM employees
GROUP BY EXTRACT(YEAR FROM hire_date)
ORDER BY COUNT(*) DESC
LIMIT 1;

-- ============================================================
-- Q8: Department with the highest total salary cost
-- ============================================================
SELECT 'Q8: Highest Salary Cost Dept' AS question,
       d.department_name              AS answer,
       SUM(e.salary)::text            AS detail
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY SUM(e.salary) DESC
LIMIT 1;

-- ============================================================
-- Q9: Projects with a budget above the average project budget
-- ============================================================
SELECT 'Q9: Above Avg Budget Projects' AS question,
       p.project_name                  AS answer,
       p.budget::text                  AS detail
FROM projects p
WHERE p.budget > (SELECT AVG(budget) FROM projects)
ORDER BY p.budget DESC;

-- ============================================================
-- Q10: Top 3 highest-paid employees in each department
-- ============================================================
WITH ranked AS (
    SELECT 
        e.name,
        d.department_name,
        e.salary,
        DENSE_RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS rnk
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
)
SELECT 'Q10: Top 3 per Dept' AS question,
       department_name       AS answer,
       name || ' (' || salary || ') rank ' || rnk AS detail
FROM ranked
WHERE rnk <= 3
ORDER BY department_name, rnk;
