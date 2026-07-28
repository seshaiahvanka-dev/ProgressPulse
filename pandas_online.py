import pandas as pd
from faker import Faker
import numpy as np

fake = Faker()

# Step 1: Generate fake student engagement data
dates = pd.date_range(start="2026-07-01", periods=20, freq="D")
data = {
    "student_id": [fake.random_int(1, 50) for _ in range(20)],   # 50 possible students
    "course_id": [fake.random_element(elements=["C1", "C2", "C3", "C4", "C5", "C6"]) for _ in range(20)],
    "login_date": dates,
    "minutes_spent": [fake.random_int(10, 120) for _ in range(20)]  # session duration
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Step 2: Identify inactive students (no login in last 7 days)
latest_date = df["login_date"].max()
cutoff_date = latest_date - pd.Timedelta(days=7)
inactive_students = df.loc[df["login_date"] < cutoff_date, "student_id"].unique()
print("\nInactive Students (no login in last 7 days):\n", inactive_students)

# Step 3: Calculate average session duration per course
avg_session_duration = df.groupby("course_id")["minutes_spent"].mean()
print("\nAverage Session Duration per Course:\n", avg_session_duration)

# Step 4: Find top 3 courses with highest engagement
top_courses = avg_session_duration.sort_values(ascending=False).head(3)
print("\nTop 3 Courses with Highest Engagement:\n", top_courses)
