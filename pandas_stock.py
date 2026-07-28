from faker import Faker
import pandas as pd
import numpy as np

fake = Faker()

# Step 1: Generate fake stock data
records = []
stock_names = [f"Stock_{i}" for i in range(1, 11)]

for day in pd.date_range("2026-01-01", periods=90, freq="D"):
    for stock in stock_names:
        open_price = fake.random_int(min=50, max=500)
        close_price = open_price + fake.random_int(min=-20, max=20)
        records.append({
            "date": day,
            "stock_name": stock,
            "open_price": open_price,
            "close_price": close_price
        })

df = pd.DataFrame(records)

# Step 2: Calculate percentage daily return
df["daily_return"] = (df["close_price"] - df["open_price"]) / df["open_price"] * 100
print("\nDaily Returns (first 5 rows):")
print(df.head())

# Step 3: Identify top gaining and losing stocks per month
df["month"] = df["date"].dt.to_period("M")
monthly_summary = df.groupby(["month", "stock_name"])["daily_return"].mean().reset_index()

top_gainers = monthly_summary.loc[monthly_summary.groupby("month")["daily_return"].idxmax()]
top_losers = monthly_summary.loc[monthly_summary.groupby("month")["daily_return"].idxmin()]

print("\nTop Gainers per Month:")
print(top_gainers)
print("\nTop Losers per Month:")
print(top_losers)

# Step 4: Compute rolling volatility (7-day window)
df["rolling_volatility"] = df.groupby("stock_name")["daily_return"].transform(lambda x: x.rolling(7).std())
print("\nRolling Volatility (first 10 rows):")
print(df.head(10))
