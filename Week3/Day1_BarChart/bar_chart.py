import matplotlib.pyplot as plt

categories = ["Python", "NumPy", "Pandas", "Matplotlib"]
hours = [8, 6, 10, 5]

plt.bar(categories, hours)
plt.title("Learning Hours by Topic")
plt.xlabel("Topic")
plt.ylabel("Hours")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()
