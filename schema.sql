CREATE TABLE users(
user_id INT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
email VARCHAR(150) NOT NULL,
role VARCHAR(100) CHECK(role IN ('Student','Instructor','Admin')),
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp);

create table courses(
course_id int primary key,
course_name varchar(120) not null,
instructor_id int,
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp,
constraint fk_instructor foreign key (instructor_id) references users(user_id) );

create table lessons(
lesson_id int primary key,
course_id int,
lesson_name varchar(120) not null,
duration_minutes int check(duration_minutes>0),
constraint fk_coursep foreign key (course_id) references courses(course_id));

create table enrollments(
enrollment_id int primary key,
user_id int,
course_id int,
status varchar(10) check(status in ('active','inactive')),
constraint fk_user foreign key(user_id) references users(user_id),
constraint fk_course foreign key(course_id) references courses(course_id),
constraint uq_enrollment unique(user_id,course_id));

create table user_activity(
activity_id int primary key,
user_id int,
lesson_id int,
activity_timestamp timestamp default current_timestamp,
constraint fk_userx foreign key(user_id) references users(user_id),
constraint fk_lesson foreign key(lesson_id) references lessons(lesson_id));

create table assessments(
assessment_id int primary key,
course_id int,
title varchar(120) not null,
max_score int check(max_score >= 0),
constraint fk_coursex foreign key(course_id) references courses(course_id));

create table assessment_submissions(
submission_id int primary key,
assessment_id int,
user_id int,
score int check (score >= 0),
constraint fk_assessment foreign key(assessment_id) references assessments(assessment_id),
constraint fk_usery foreign key(user_id) references users(user_id),
constraint uq_submission unique(assessment_id,user_id));







