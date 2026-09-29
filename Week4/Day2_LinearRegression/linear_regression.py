import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Score": [50, 55, 61, 66, 72, 78, 84, 90]
})

X = df[["StudyHours"]]
y = df["Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual scores:")
print(y_test.to_list())

print("\nPredicted scores:")
print([round(value, 2) for value in predictions])

print("\nCoefficient:", round(model.coef_[0], 2))
print("Intercept:", round(model.intercept_, 2))
