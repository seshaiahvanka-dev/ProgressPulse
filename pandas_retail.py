import pandas as pd
from faker import Faker
import numpy as np


fake = Faker()

data = {
    'order_id' : np.arange(1,21),
    'customer_id' : [fake.random_int(min=100,max=200) for i in range(20)],
    'order_date' : [fake.date_between(start_date='-6M', end_date='today') for i in range(20)],
    'order_amount' : [fake.random_int(min=100,max=1000) for i in range(20)]
}
df = pd.DataFrame(data)
print('Original Data:\n',df)

df["order_date"] = pd.to_datetime(df["order_date"])

df["month"] = df["order_date"].dt.to_period("M")

monthly_revenue = df.groupby("month")["order_amount"].sum()
print("\nMonthly Total Revenue:\n", monthly_revenue)

unique_customers = df.groupby("month")["customer_id"].nunique()

best_month = unique_customers.idxmax()
print(f"\nMonth with highest unique customers: {best_month}")