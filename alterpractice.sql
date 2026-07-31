ALTER TABLE Students ADD email varchar(100);

ALTER TABLE Students
ADD phone BIGINT;

ALTER TABLE Students
MODIFY student_name VARCHAR(100);

ALTER TABLE Students
RENAME COLUMN marks TO total_marks;

ALTER TABLE Student_Details
RENAME TO Students;

ALTER TABLE Students
DROP COLUMN email;

ALTER TABLE Students
ADD CONSTRAINT uq_phone UNIQUE (phone);

ALTER TABLE Students
ADD CONSTRAINT chk_marks
CHECK (total_marks BETWEEN 0 AND 100);

ALTER TABLE Students
MODIFY student_name VARCHAR(100) NOT NULL;

DESC Students;