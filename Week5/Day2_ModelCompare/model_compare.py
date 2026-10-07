from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)
tree_accuracy = accuracy_score(y_test, tree.predict(X_test))

forest = RandomForestClassifier(n_estimators=100, random_state=42)
forest.fit(X_train, y_train)
forest_accuracy = accuracy_score(y_test, forest.predict(X_test))

print("Decision Tree Accuracy:", round(tree_accuracy, 4))
print("Random Forest Accuracy:", round(forest_accuracy, 4))

if forest_accuracy > tree_accuracy:
    print("Random Forest performed better on this test set.")
elif tree_accuracy > forest_accuracy:
    print("Decision Tree performed better on this test set.")
else:
    print("Both models had the same test accuracy.")
