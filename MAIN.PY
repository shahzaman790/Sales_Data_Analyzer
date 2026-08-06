import pandas as pd

# CSV file read karna
data = pd.read_csv("sales.csv")

print("===== SALES DATA =====")
print(data)

# Total Sales
total_sales = data["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Average Sales
average_sales = data["Sales"].mean()
print("Average Sales:", round(average_sales, 2))

# Best Selling Product
top_product = data.loc[data["Sales"].idxmax()]
print("\nBest Selling Product:", top_product["Product"])
print("Sales:", top_product["Sales"])
import matplotlib.pyplot as plt

# Bar Chart
plt.bar(data["Product"], data["Sales"])

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()