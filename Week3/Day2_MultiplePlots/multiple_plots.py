import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 145, 135, 170, 190]
expenses = [80, 95, 90, 105, 115]
products = ["Product A", "Product B", "Product C", "Product D"]
units = [35, 50, 42, 60]

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(products, units)
plt.title("Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o", label="Sales")
plt.plot(months, expenses, marker="s", label="Expenses")
plt.title("Sales vs Expenses")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
