insert into users(user_id, name, email, role)
values (1,'Arjun Rao','arjun.rao@example.com','Student'),
(2,'Meera Iyer','meera.iyer@example.com','Student'),
(3,'Ravi Kumar','ravi.kumar@example.com','Instructor'),
(4,'Sneha Rani','sneha.rani@example.com','Student'),
(5,'Kiran Das','kiran.das@example.com','Instructor'),
(6,'Priya Shah','priya.shah@example.com','Admin');

insert into courses(course_id,course_name,instructor_id)
values
(1,'Java Basics',3),
(2,'Python Fundamentals',5),
(3,'Web Development',3),
(4,'Database management',5),
(5,'DSA',3);

insert into lessons
values
(1,1,'Introduction to Java',45),
(2,1,'Java OOP Concepts',60),
(3,2,'Python Basics',40),
(4,2,'Python Data Structures',55),
(5,3,'HTML & CSS',50),
(6,3,'JavaScript Essentials',60),
(7,4,'SQL Basics',45),
(8,4,'Normalization Concepts',50),
(9,5,'Arrays & LinkedLists',60),
(10,5,'Recursion Techniques',70);

insert into enrollments
values
(1,1,1,'active'),
(2,2,1,'active'),
(3,4,2,'active'),
(4,1,3,'inactive'),
(5,2,4,'active'),
(6,4,5,'active');

insert into user_activity(activity_id,user_id,lesson_id)
values
(1,1,1),
(2,2,2),
(3,4,3),
(4,1,5),
(5,2,7),
(6,4,9);

insert into assessments
values
(1,1,'Java Basics Quiz',100),
(2,1,'Java OOP Assignment',50),
(3,2,'Python Fundamentals MCQ',100),
(4,3,'Web Dev Project',75),
(5,4,'SQL Test',100),
(6,5,'DSA Midterm',100);

insert into assessment_submissions
values
(1,1,1,85),
(2,1,2,90),
(3,2,4,40),
(4,3,1,95),
(5,3,2,88),
(6,4,4,70),
(7,5,1,92),
(8,6,2,80);




