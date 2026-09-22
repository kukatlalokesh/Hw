import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
scores = np.random.normal(loc=75, scale=10, size=200)

plt.hist(scores, bins=10, edgecolor="black")
plt.title("Distribution of Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
