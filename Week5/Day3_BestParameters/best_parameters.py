from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

X, y = load_iris(return_X_y=True)
search = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    {"max_depth": [2, 3, 4, 5], "min_samples_split": [2, 4, 6]},
    cv=5,
    scoring="accuracy"
)
search.fit(X, y)
print("Best settings:", search.best_params_)
print("Best average validation accuracy:", round(search.best_score_, 4))
print("These settings had the highest average accuracy among the tested combinations.")
print("Cross-validation helps compare settings, but performance on new data can differ.")
