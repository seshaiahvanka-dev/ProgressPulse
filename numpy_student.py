import numpy as np

# Step 1: Create random marks for 200 students across 6 subjects
marks = np.random.randint(30, 100, size=(200, 6)).astype(float)

# Step 2: Calculate total and percentage scores
totals = marks.sum(axis=1)
percentages = totals / (6 * 100) * 100  # out of 600 marks

# Step 3: Assign grades using vectorized operations
grades = np.where(percentages >= 90, "A+",
         np.where(percentages >= 75, "A",
         np.where(percentages >= 60, "B",
         np.where(percentages >= 50, "C", "F"))))

# Step 4: Identify top 10% performers
threshold = np.percentile(percentages, 90)
top_students = np.where(percentages >= threshold)[0]

print("Total Scores (first 5):", totals[:5])
print("Percentages (first 5):", percentages[:5])
print("Grades (first 5):", grades[:5])
print("Top 10% Performers (indices):", top_students)
