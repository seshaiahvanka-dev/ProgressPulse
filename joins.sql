USE Joins;
insert into departments values(70,"dance");
SELECT * FROM departments;
SELECT * FROM employees;

#inner join-returns only matching values from both tables

select * from departments d inner join employees e on e.dept_id=d.dept_id;
SELECT d.dept_name,sum(e.salary) as total_salary
From departments d inner join employees e on e.dept_id=
d.dept_id
group by d.dept_name;

#natural join combines the tables by columns that have same name and on clause is not specified.
select * from departments d natural join employees e;

select * from departments d right join  
employees e on e.dept_id=d.dept_id;

(select * from departments d left join employees e on e.dept_id=d.dept_id) union (select * from departments d right join employees e on e.dept_id=d.dept_id);

select * from employees e cross join departments;

CREATE INDEX idx_dept_salary
ON employees(dept_id, salary);

SELECT *
FROM employees
WHERE dept_id = 10
AND salary > 5000000;
#gives execution plan
EXPLAIN
SELECT *
FROM employees
WHERE emp_name = 'Ravi';

SHOW INDEX FROM employees;