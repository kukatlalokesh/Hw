import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 145, 135, 170, 190]
expenses = [80, 95, 90, 105, 115]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker="o", linewidth=2, label="Sales")
plt.plot(months, expenses, marker="s", linewidth=2, label="Expenses")

plt.title("Monthly Sales and Expenses")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
