import pandas as pd
from faker import Faker
import numpy as np

fake = Faker()

# Step 1: Generate fake weather data
dates = pd.date_range(start="2026-07-01", periods=10, freq="D")
data = {
    "date": dates,
    "city": [fake.random_element(elements=["Bengaluru", "Delhi", "Mumbai"]) for _ in range(10)],
    "temperature": [fake.random_int(20, 40) for _ in range(10)],
    "humidity": [fake.random_int(40, 90) for _ in range(10)]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Step 2: Filter for a single city (e.g., Bengaluru)
city_df = df[df["city"] == "Bengaluru"]
print("\nFiltered Data (Bengaluru):\n", city_df)

# Step 3: Rolling 3-day average temperature
city_df["rolling_avg_temp"] = city_df["temperature"].rolling(window=3).mean()
print("\nRolling 3-Day Average Temperature:\n", city_df[["date", "temperature", "rolling_avg_temp"]])

# Step 4: Detect days where humidity increased compared to previous day
city_df["humidity_increase"] = city_df["humidity"].diff() > 0
print("\nHumidity Increase Days:\n", city_df[["date", "humidity", "humidity_increase"]])
