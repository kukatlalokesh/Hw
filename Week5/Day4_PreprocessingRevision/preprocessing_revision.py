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

X = df.drop(columns="Passed")
y = df["Passed"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
numeric = Pipeline([("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())])
preprocessor = ColumnTransformer([
    ("numeric", numeric, ["Age", "StudyHours"]),
    ("category", OneHotEncoder(handle_unknown="ignore"), ["Department"])
])
X_train_ready = preprocessor.fit_transform(X_train)
X_test_ready = preprocessor.transform(X_test)
print("Training rows:", X_train_ready.shape)
print("Testing rows:", X_test_ready.shape)
print("Missing values before preprocessing:", df.isna().sum().to_dict())
