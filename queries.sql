-- 1. Retrieve employee names along with their department names
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- 2. Find the top 3 highest-paid employees in each department
SELECT employee_id, name, department_id, salary
FROM (
    SELECT employee_id, name, department_id, salary,
           RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank
    FROM employees
) ranked
WHERE rank <= 3;

-- 3. Show customers and their most recent order date
SELECT c.customer_id, c.name, MAX(o.order_date) AS last_order
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;

-- 4. List students who share the same marks in a subject
SELECT s1.student_id, s2.student_id, s1.subject_id, s1.marks
FROM results s1
JOIN results s2
  ON s1.subject_id = s2.subject_id
 AND s1.marks = s2.marks
 AND s1.student_id < s2.student_id;

-- 5. Display products that were never ordered
SELECT p.product_id, p.product_name
FROM products p
LEFT JOIN order_details od ON p.product_id = od.product_id
WHERE od.product_id IS NULL;

-- 6. Find employees with the longest tenure
SELECT employee_id, name, join_date
FROM employees
ORDER BY join_date ASC
LIMIT 5;

-- 7. Show average salary per department, including departments with no employees
SELECT d.department_id, d.department_name, AVG(e.salary) AS avg_salary
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name;

-- 8. Retrieve orders where the total amount is greater than the average order amount
SELECT order_id, SUM(amount) AS total_amount
FROM orders
GROUP BY order_id
HAVING SUM(amount) > (SELECT AVG(amount) FROM orders);

-- 9. Get employees who have the same manager
SELECT manager_id, GROUP_CONCAT(name) AS team_members
FROM employees
WHERE manager_id IS NOT NULL
GROUP BY manager_id;

-- 10. Display the cumulative sales per month
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(amount) AS monthly_sales,
       SUM(SUM(amount)) OVER (ORDER BY DATE_TRUNC('month', order_date)) AS cumulative_sales
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;
