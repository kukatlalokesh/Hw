"""Week 6 Monday coding test: trees, random forest, and preprocessing."""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Task 1: Build and evaluate a decision tree.
tree = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("classifier", DecisionTreeClassifier(max_depth=3, random_state=42)),
])
tree.fit(X_train, y_train)
tree_predictions = tree.predict(X_test)
print("Decision tree accuracy:", round(accuracy_score(y_test, tree_predictions), 4))

# Task 2: Build and evaluate a random forest on the same split.
forest = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42)),
])
forest.fit(X_train, y_train)
forest_predictions = forest.predict(X_test)
print("Random forest accuracy:", round(accuracy_score(y_test, forest_predictions), 4))

# Task 3: Explain why imputation belongs inside the pipeline:
# The imputer learns only from the training split, avoiding data leakage.
