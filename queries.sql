-- Aug 14 Advanced SQL Problems with Solutions

-- 1. Find employees who earn more than the average salary of their department.
SELECT e1.name, e1.department, e1.salary
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary) FROM employees e2 WHERE e2.department = e1.department
);

-- 2. Rank employees within each department by salary.
SELECT name, department, salary,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;

-- 3. Categorize employees based on salary ranges (High, Medium, Low).
SELECT name, salary,
       CASE 
           WHEN salary >= 60000 THEN 'High'
           WHEN salary BETWEEN 40000 AND 59999 THEN 'Medium'
           ELSE 'Low'
       END AS salary_category
FROM employees;

-- 4. Show departments with total salary expenditure greater than 100000.
WITH dept_totals AS (
    SELECT department, SUM(salary) AS total_salary
    FROM employees
    GROUP BY department
)
SELECT * FROM dept_totals WHERE total_salary > 100000;

-- 5. Find the highest-paid employee in each department.
SELECT name, department, salary
FROM employees
WHERE salary IN (
    SELECT MAX(salary) FROM employees GROUP BY department
);

-- 6. Show employees whose salary is above the overall company average.
SELECT name, department, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 7. Update salaries of IT department employees by 10%.
UPDATE employees SET salary = salary * 1.10 WHERE department = 'IT';

-- 8. Delete employees with salary less than 30000.
DELETE FROM employees WHERE salary < 30000;
