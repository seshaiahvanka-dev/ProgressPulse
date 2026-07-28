from faker import Faker
import pandas as pd
import numpy as np

fake = Faker()

# Step 1: Generate fake student marks data
records = []
subjects = ["Math", "Science", "English", "History", "Geography", "Computer"]

for student_id in range(1, 201):  # 200 students
    for subject in subjects:
        records.append({
            "student_id": student_id,
            "subject": subject,
            "marks": fake.random_int(min=30, max=100),
            "exam_date": fake.date_between(start_date="-30d", end_date="today")
        })

df = pd.DataFrame(records)

# Step 2: Compute subject-wise pass percentage (pass = marks >= 40)
pass_percentage = df.groupby("subject").apply(lambda x: (x["marks"] >= 40).mean() * 100)
print("\nSubject-wise Pass Percentage:")
print(pass_percentage)

# Step 3: Identify students failing in more than one subject
fail_counts = df[df["marks"] < 40].groupby("student_id")["subject"].count()
failing_students = fail_counts[fail_counts > 1]
print("\nStudents failing in more than one subject:")
print(failing_students)

# Step 4: Generate performance summary report (average marks per student)
summary = df.groupby("student_id")["marks"].mean().reset_index()
summary.rename(columns={"marks": "average_marks"}, inplace=True)
print("\nPerformance Summary Report (first 5 rows):")
print(summary.head())
