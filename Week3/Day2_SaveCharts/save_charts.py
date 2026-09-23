import matplotlib.pyplot as plt
from pathlib import Path

output_folder = Path(__file__).parent / "charts"
output_folder.mkdir(exist_ok=True)

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 145, 135, 170, 190]

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True, alpha=0.3)
plt.tight_layout()

output_file = output_folder / "monthly_sales.png"
plt.savefig(output_file, dpi=150, bbox_inches="tight")
print(f"Chart saved to: {output_file}")

plt.show()
