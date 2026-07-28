import numpy as np

# Step 1: Generate fake hourly temperature readings (7 days × 24 hours)
np.random.seed(42)  # reproducibility
temps = np.random.randint(15, 40, size=(7, 24))  # temperatures between 15°C and 40°C

print("Original Temperatures (Day 1):\n", temps[0])

# Step 2: Daily maximum and minimum temperature
daily_max = temps.max(axis=1)  # max per day
daily_min = temps.min(axis=1)  # min per day
print("\nDaily Max Temperatures:", daily_max)
print("Daily Min Temperatures:", daily_min)

# Step 3: Identify the day with the largest temperature variation
variation = daily_max - daily_min
largest_var_day = np.argmax(variation) + 1  # +1 for human-friendly day numbering
print("\nDay with largest variation:", largest_var_day)

# Step 4: Replace outliers beyond ±2 standard deviations with mean temperature
mean_temp = temps.mean()
std_temp = temps.std()
lower, upper = mean_temp - 2*std_temp, mean_temp + 2*std_temp

temps_cleaned = np.where((temps < lower) | (temps > upper), mean_temp, temps)
print("\nCleaned Temperatures (Day 1):\n", temps_cleaned[0])
