import numpy as np

# Step 1: Generate fake performance ratings (100 employees × 4 quarters)
np.random.seed(42)  # reproducibility
ratings = np.random.randint(1, 6, size=(100, 4))  # values between 1–5

print("Original Ratings:\n", ratings)

# Step 2: Min-Max Normalization
# Formula: (x - min) / (max - min)
min_val = ratings.min()
max_val = ratings.max()
normalized = (ratings - min_val) / (max_val - min_val)

print("\nNormalized Ratings:\n", normalized)

# Step 3: Average rating per employee (row-wise mean)
employee_avg = normalized.mean(axis=1)
print("\nAverage Rating per Employee:\n", employee_avg)

# Step 4: Company mean
company_mean = employee_avg.mean()
print("\nCompany Mean Rating:", company_mean)

# Step 5: Employees above company mean
above_mean = np.where(employee_avg > company_mean)[0] + 1  # +1 for employee numbering
print("\nEmployees above company mean:\n", above_mean)
