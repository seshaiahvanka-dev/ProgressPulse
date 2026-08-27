SELECT customer_name, product, (quantity * price) AS total_value
FROM orders
ORDER BY total_value DESC
LIMIT 2;

SELECT product, SUM(quantity * price) AS total_sales
FROM orders
GROUP BY product
ORDER BY total_sales DESC;

SELECT customer_name, SUM(quantity) AS total_items
FROM orders
GROUP BY customer_name
HAVING SUM(quantity) > 1;

SELECT order_id, customer_name, product, price
FROM orders
WHERE price > (SELECT AVG(price) FROM orders);

SELECT order_id, customer_name, product, quantity, price,
       RANK() OVER (ORDER BY quantity * price DESC) AS order_rank
FROM orders;

WITH daily_sales AS (
    SELECT order_date, SUM(quantity * price) AS total_sales
    FROM orders
    GROUP BY order_date
)
SELECT * FROM daily_sales WHERE total_sales > 10000;

UPDATE orders SET price = price * 0.95 WHERE product = 'Laptop';

DELETE FROM orders WHERE order_date < '2026-08-02';
