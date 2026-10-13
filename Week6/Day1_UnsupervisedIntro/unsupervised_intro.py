"""Unsupervised learning groups observations without target labels."""
import pandas as pd
from sklearn.cluster import KMeans

customers = pd.DataFrame({
    "Visits": [1, 2, 2, 3, 8, 9, 9, 10],
    "Spending": [10, 12, 15, 18, 75, 80, 85, 90],
})
print("Input data (no labels):")
print(customers)

model = KMeans(n_clusters=2, random_state=42, n_init=10)
customers["Cluster"] = model.fit_predict(customers[["Visits", "Spending"]])
print("\nGroups found by KMeans:")
print(customers)
print("\nCluster numbers identify groups; they are not predefined classes.")
