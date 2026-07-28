import pandas as pd
from faker import Faker
import numpy as np

fake = Faker()

# Step 1: Generate fake employee performance data
data = {
    "emp_id": np.arange(1, 21),  # 20 employees
    "department": [fake.random_element(elements=["HR", "IT", "Finance", "Sales"]) for _ in range(20)],
    "quarter": [fake.random_element(elements=["Q1", "Q2", "Q3", "Q4"]) for _ in range(20)],
    "performance_score": [fake.random_int(1, 5) for _ in range(20)]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Step 2: Group by department and quarter
grouped = df.groupby(["department", "quarter"])["performance_score"].mean()
print("\nQuarter-wise Average Performance per Department:\n", grouped)

# Step 3: Pivot table for department vs quarter
pivot = df.pivot_table(index="department", columns="quarter", values="performance_score", aggfunc="mean")
print("\nPivot Table (Department vs Quarter):\n", pivot)

# Step 4: Identify departments with consistent improvement (non-decreasing trend)
improving = []
for dept, row in pivot.iterrows():
    scores = row.dropna().values  # ignore missing quarters
    if len(scores) > 1 and all(scores[i] <= scores[i+1] for i in range(len(scores)-1)):
        improving.append(dept)

print("\nDepartments with consistent improvement:\n", improving)
