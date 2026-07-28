import numpy as np

# Step 1: Create random heart rate data for 60 patients over 24 hours
# Use float dtype so we can insert NaN values
heart_rates = np.random.randint(50, 150, size=(60, 24)).astype(float)

# Step 2: Compute hourly average heart rate (mean across patients for each hour)
hourly_avg = heart_rates.mean(axis=0)
print("Hourly Average Heart Rate:")
print(hourly_avg)

# Step 3: Detect abnormal readings (outside normal range 60-100 bpm)
abnormal = (heart_rates < 60) | (heart_rates > 100)
print("\nNumber of abnormal readings:", abnormal.sum())

# Step 4: Replace missing values using forward fill logic
# Simulate missing values
heart_rates[0, 5] = np.nan
heart_rates[2, 10] = np.nan

# Forward fill row by row
for i in range(heart_rates.shape[0]):
    for j in range(heart_rates.shape[1]):
        if np.isnan(heart_rates[i, j]):
            # If first column is NaN, replace with row average
            if j == 0:
                heart_rates[i, j] = np.nanmean(heart_rates[i])
            else:
                heart_rates[i, j] = heart_rates[i, j-1]

print("\nMissing values handled with forward fill.")
