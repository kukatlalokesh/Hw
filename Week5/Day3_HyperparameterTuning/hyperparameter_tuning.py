from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier(random_state=42)
parameters = {"max_depth": [2, 3, 4, 5], "min_samples_split": [2, 4, 6]}
search = GridSearchCV(model, parameters, cv=5, scoring="accuracy")
search.fit(X, y)
print("Best parameters:", search.best_params_)
print("Best cross-validation accuracy:", round(search.best_score_, 4))
