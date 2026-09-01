-- 1. Retrieve all employees who joined after 2020
SELECT employee_id, name, join_date
FROM employees
WHERE join_date > '2020-01-01';

-- 2. Find the top 5 highest-paid employees
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 5;

-- 3. Count the number of students enrolled in each course
SELECT course_id, COUNT(student_id) AS total_enrolled
FROM enrollments
GROUP BY course_id;

-- 4. Get customers who placed more than 3 orders
SELECT customer_id, COUNT(order_id) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 3;

-- 5. Display average marks per subject
SELECT subject_id, AVG(marks) AS avg_marks
FROM results
GROUP BY subject_id;

-- 6. List products with stock less than 10
SELECT product_id, product_name, stock
FROM products
WHERE stock < 10;

-- 7. Show departments with more than 20 employees
SELECT department_id, COUNT(employee_id) AS dept_size
FROM employees
GROUP BY department_id
HAVING COUNT(employee_id) > 20;

-- 8. Find orders placed in the last 30 days
SELECT order_id, order_date, customer_id
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '30 days';

-- 9. Get students who scored above 90 in Mathematics
SELECT student_id, name, marks
FROM results
WHERE subject = 'Mathematics' AND marks > 90;

-- 10. Retrieve employees with NULL manager_id (top-level managers)
SELECT employee_id, name
FROM employees
WHERE manager_id IS NULL;
