import pandas as pd

df = pd.DataFrame({
    "Age": [22, 25, None, 35, 29, 42, 31, None, 27, 38, 24, 45],
    "StudyHours": [2, 4, 3, 7, 5, 8, 6, 4, 3, 9, 5, 8],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT",
                   "Finance", "HR", "IT", "Finance", "HR", "IT"],
    "Passed": [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1]
})

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

X = df.drop(columns="Passed")
y = df["Passed"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
preprocessor = ColumnTransformer([
    ("numbers", numeric_pipeline, ["Age", "StudyHours"]),
    ("categories", OneHotEncoder(handle_unknown="ignore"), ["Department"])
])
model = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", LogisticRegression(max_iter=300))
])
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Actual:", y_test.to_list())
print("Predicted:", predictions.tolist())
print("Accuracy:", round(accuracy_score(y_test, predictions), 4))
print(classification_report(y_test, predictions, zero_division=0))
print("Note: This tiny example is for practice, not a reliable performance estimate.")
