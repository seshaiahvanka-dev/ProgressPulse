import numpy as np

# Step 1: Generate fake time spent data (14 days × 6 courses)
np.random.seed(42)  # reproducibility
time_spent = np.random.randint(10, 120, size=(14, 6))  # minutes between 10–120

print("Original Data (Day 1):\n", time_spent[0])

# Step 2: Compute total time spent per course
total_time_per_course = time_spent.sum(axis=0)  # sum column-wise
print("\nTotal Time Spent per Course:\n", total_time_per_course)

# Step 3: Identify courses where average daily engagement exceeds threshold
threshold = 60  # minutes per day
avg_daily_engagement = time_spent.mean(axis=0)
above_threshold = np.where(avg_daily_engagement > threshold)[0] + 1  # +1 for course numbering
print("\nAverage Daily Engagement per Course:\n", avg_daily_engagement)
print("Courses above threshold:", above_threshold)

# Step 4: Rank courses based on engagement
ranked_courses = np.argsort(total_time_per_course)[::-1] + 1  # descending order
print("\nCourses ranked by engagement (highest to lowest):\n", ranked_courses)
