import numpy as np

# Step 1: Create random stock prices for 10 companies over 90 days
# Shape: (10 stocks, 90 days)
prices = np.random.randint(50, 500, size=(10, 90)).astype(float)

# Step 2: Calculate daily returns
# Formula: (price_today - price_yesterday) / price_yesterday
daily_returns = (prices[:, 1:] - prices[:, :-1]) / prices[:, :-1]

print("Daily Returns (first 2 stocks, first 5 days):")
print(daily_returns[:2, :5])

# Step 3: Compute volatility (standard deviation of returns per stock)
volatility = daily_returns.std(axis=1)
print("\nVolatility per stock:")
print(volatility)

# Step 4: Identify the stock with the highest risk (highest volatility)
highest_risk_stock = np.argmax(volatility)
print("\nStock with highest risk:", highest_risk_stock)
