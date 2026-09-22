import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [120, 150, 135, 180, 210]

plt.plot(days, sales, marker="o")
plt.title("Weekly Sales")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
