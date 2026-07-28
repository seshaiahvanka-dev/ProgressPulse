import numpy as np
from faker import Faker


fake = Faker()

np.random.seed(42)
sales = np.random.randint(-10,100,size=(30,5))

print("Original Sales Data:\n",sales)

sales[sales<0] = 0
print("Cleaned Sales Data:\n",sales)

weeks = sales[:28].reshape(4,7,5)
weekly_avg = weeks.mean(axis=1)
product_weekly_avg = weekly_avg.mean(axis=0)
print("Average weekly Sales per product:\n",product_weekly_avg)

best_product = np.argmax(product_weekly_avg)+1
print(f"Product {best_product} has the highest average weekly sales.")


