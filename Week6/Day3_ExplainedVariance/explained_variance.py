"""Inspect how much variance each principal component preserves."""
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(load_iris().data)
pca = PCA().fit(X)
total = 0
for index, ratio in enumerate(pca.explained_variance_ratio_, start=1):
    total += ratio
    print(f"PC{index}: {ratio:.2%} variance, cumulative: {total:.2%}")
print("Variance retained by first two components:",
      f"{sum(pca.explained_variance_ratio_[:2]):.2%}")
