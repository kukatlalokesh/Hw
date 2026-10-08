from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print("5-fold accuracy scores:", scores)
print("Average accuracy:", round(scores.mean(), 4))
