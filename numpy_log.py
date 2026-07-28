import numpy as np

# Step 1: Create random request counts per minute for 24 hours
# 24 hours × 60 minutes = 1440 values
requests = np.random.randint(50, 500, size=1440).astype(float)

# Step 2: Identify peak traffic hours
# Reshape into (24 hours, 60 minutes) and sum per hour
hourly_requests = requests.reshape(24, 60).sum(axis=1)
peak_hours = np.where(hourly_requests == hourly_requests.max())[0]

print("Hourly Requests:", hourly_requests)
print("Peak Traffic Hours:", peak_hours)

# Step 3: Smooth data using moving average (window = 5 minutes)
def moving_average(data, window=5):
    return np.convolve(data, np.ones(window)/window, mode='valid')

smoothed = moving_average(requests, window=5)
print("\nSmoothed Data (first 10 values):", smoothed[:10])

# Step 4: Detect sudden traffic spikes (difference > 200 requests in one minute)
diffs = np.diff(requests)
spikes = np.where(diffs > 200)[0]
print("\nSudden Traffic Spikes at minutes:", spikes)
