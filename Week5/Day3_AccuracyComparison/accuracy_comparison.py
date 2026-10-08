import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True)
models = {
    "Decision Tree": DecisionTreeClassifier(max_depth=3, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=300),
    "KNN": KNeighborsClassifier(n_neighbors=5)
}
results = []
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
    results.append({"Model": name, "Mean Accuracy": round(scores.mean(), 4)})
table = pd.DataFrame(results).sort_values("Mean Accuracy", ascending=False)
print("5-fold Cross-validation Model Comparison:")
print(table.to_string(index=False))
