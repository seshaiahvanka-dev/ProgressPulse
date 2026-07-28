from faker import Faker
import pandas as pd
import numpy as np

fake = Faker()

# Step 1: Generate fake patient heart rate data
records = []
for _ in range(500):  # 500 readings
    records.append({
        "patient_id": fake.random_int(min=1, max=60),
        "timestamp": fake.date_time_between(start_date="-1d", end_date="now"),
        "heart_rate": fake.random_int(min=50, max=150),
        "ward": fake.random_element(elements=("ICU", "General", "Emergency"))
    })

df = pd.DataFrame(records)

# Step 2: Compute average heart rate per ward
avg_per_ward = df.groupby("ward")["heart_rate"].mean()
print("\nAverage Heart Rate per Ward:")
print(avg_per_ward)

# Step 3: Identify patients with sudden spikes (difference > 30 bpm between readings)
df_sorted = df.sort_values(by=["patient_id", "timestamp"])
df_sorted["diff"] = df_sorted.groupby("patient_id")["heart_rate"].diff()
spikes = df_sorted[df_sorted["diff"].abs() > 30]
print("\nPatients with sudden spikes in heart rate:")
print(spikes.head())

# Step 4: Extract critical cases (heart_rate < 50 or > 120)
critical_cases = df[(df["heart_rate"] < 50) | (df["heart_rate"] > 120)]
print("\nCritical Cases:")
print(critical_cases.head())
