from faker import Faker
import pandas as pd
import numpy as np

fake = Faker()

# Step 1: Generate 1000 fake transactions
records = []
for _ in range(1000):
    records.append({
        "account_id": fake.random_int(min=1, max=50),
        "transaction_date": fake.date_between(start_date="-20d", end_date="today"),
        "amount": fake.random_int(min=-5000, max=5000),
        "transaction_type": fake.random_element(elements=("debit", "credit"))
    })

df = pd.DataFrame(records)

# Step 2: Aggregate daily totals per account
daily_totals = df.groupby(["account_id", "transaction_date"])["amount"].sum().reset_index()
print("\nDaily Totals (first 5 rows):")
print(daily_totals.head())

# Step 3: Find accounts with unusually high transaction volume
volume_per_account = df.groupby("account_id")["amount"].count()
threshold = volume_per_account.mean() + 3 * volume_per_account.std()
high_volume_accounts = volume_per_account[volume_per_account > threshold]
print("\nHigh Volume Accounts:")
print(high_volume_accounts)

# Step 4: Detect potential fraud (transactions far from average)
mean_amt = df["amount"].mean()
std_amt = df["amount"].std()
fraud_threshold = mean_amt + 3 * std_amt

potential_fraud = df[df["amount"].abs() > fraud_threshold]
print("\nPotential Fraud Transactions (first 5 rows):")
print(potential_fraud.head())
