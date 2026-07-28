import numpy as np

# Step 1: Create random transactions for 50 accounts over 20 days
transactions = np.random.randint(-5000, 5000, size=(50, 20))

# Step 2: Separate debit (negative) and credit (positive)
debit = np.where(transactions < 0, transactions, 0)
credit = np.where(transactions > 0, transactions, 0)

# Step 3: Compute daily net balance (sum of all accounts per day)
daily_net = transactions.sum(axis=0)

# Step 4: Find accounts with all negative transactions
continuous_negative = np.all(transactions < 0, axis=1)
accounts_with_negative_trend = np.where(continuous_negative)[0]

# Step 5: Print results
print("Daily Net Balance (20 days):")
print(daily_net)
print("\nAccounts with continuous negative trend:")
print(accounts_with_negative_trend)
