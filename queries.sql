-- 1. Find employees earning above the company average salary
SELECT employee_id, name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 2. Show customers who never placed an order
SELECT customer_id, name
FROM customers
WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM orders);

-- 3. Display the second highest salary in the company
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- 4. Get products purchased by more than 50 unique customers
SELECT product_id, COUNT(DISTINCT customer_id) AS buyers
FROM order_details
GROUP BY product_id
HAVING COUNT(DISTINCT customer_id) > 50;

-- 5. Retrieve employees working in both 'HR' and 'Finance'
SELECT employee_id, name
FROM employees
WHERE department IN ('HR', 'Finance')
GROUP BY employee_id, name
HAVING COUNT(DISTINCT department) = 2;

-- 6. List top 3 courses with highest enrollment
SELECT course_id, COUNT(student_id) AS total_enrolled
FROM enrollments
GROUP BY course_id
ORDER BY total_enrolled DESC
LIMIT 3;

-- 7. Show customers with orders totaling more than $10,000
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 10000;

-- 8. Find employees whose names start and end with the same letter
SELECT employee_id, name
FROM employees
WHERE LEFT(name, 1) = RIGHT(name, 1);

-- 9. Display students who scored the highest in each subject
SELECT subject_id, student_id, marks
FROM results r
WHERE marks = (
    SELECT MAX(marks)
    FROM results
    WHERE subject_id = r.subject_id
);

-- 10. Get average order value per customer
SELECT customer_id, AVG(amount) AS avg_order_value
FROM orders
GROUP BY customer_id;
