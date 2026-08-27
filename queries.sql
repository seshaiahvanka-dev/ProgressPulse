
-- 1. Find the 3 most expensive products ordered
SELECT product, price
FROM orders
ORDER BY price DESC
LIMIT 3;

-- 2. Show customers who bought laptops and also bought another product
SELECT DISTINCT o1.customer_name
FROM orders o1
JOIN orders o2 ON o1.customer_name = o2.customer_name
WHERE o1.product = 'Laptop' AND o2.product <> 'Laptop';

-- 3. Calculate running total of sales by date
SELECT order_date, SUM(quantity * price) OVER (ORDER BY order_date) AS running_total
FROM orders;

-- 4. Find customers who spent more than the average spending
SELECT customer_name, SUM(quantity * price) AS total_spent
FROM orders
GROUP BY customer_name
HAVING SUM(quantity * price) > (SELECT AVG(quantity * price) FROM orders);

-- 5. Show product sales percentage contribution
SELECT product,
       ROUND(SUM(quantity * price) * 100.0 / (SELECT SUM(quantity * price) FROM orders), 2) AS percentage_contribution
FROM orders
GROUP BY product;

-- 6. Find duplicate orders (same customer, product, and date)
SELECT customer_name, product, order_date, COUNT(*) AS duplicate_count
FROM orders
GROUP BY customer_name, product, order_date
HAVING COUNT(*) > 1;

-- 7. Use LEAD to compare next day’s sales
SELECT order_date, SUM(quantity * price) AS daily_sales,
       LEAD(SUM(quantity * price)) OVER (ORDER BY order_date) AS next_day_sales
FROM orders
GROUP BY order_date;

-- 8. Delete orders with quantity = 0
DELETE FROM orders WHERE quantity = 0;
