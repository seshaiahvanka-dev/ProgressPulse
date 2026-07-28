from faker import Faker
import pandas as pd
import numpy as np

fake = Faker()

# Step 1: Generate fake log data
records = []
endpoints = ["/home", "/login", "/checkout", "/api/data"]

# Use freq="min" instead of "T"
for minute in pd.date_range("2026-07-21", periods=200, freq="min"):
    for ep in endpoints:
        records.append({
            "timestamp": minute,
            "endpoint": ep,
            "response_time": fake.random_int(min=50, max=500)  # ms
        })

df = pd.DataFrame(records)

# Step 2: Compute average response time per endpoint
avg_response = df.groupby("endpoint")["response_time"].mean()
print("\nAverage Response Time per Endpoint:")
print(avg_response)

# Step 3: Identify endpoints exceeding SLA threshold (e.g., > 300 ms)
sla_threshold = 300
exceeding = df.groupby("endpoint")["response_time"].mean()
exceeding = exceeding[exceeding > sla_threshold]
print("\nEndpoints exceeding SLA threshold:")
print(exceeding)

# Step 4: Detect time windows with performance degradation
# Rolling average over 10 minutes
df["rolling_avg"] = df.groupby("endpoint")["response_time"].transform(lambda x: x.rolling(10).mean())
degraded = df[df["rolling_avg"] > sla_threshold]
print("\nPerformance Degradation (first 5 rows):")
print(degraded.head())
