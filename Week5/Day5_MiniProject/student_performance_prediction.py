"""Week 5 mini project: predict student final scores using two regression models."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data_path = Path(__file__).with_name("students.csv")
df = pd.read_csv(data_path)
print("Dataset preview:")
print(df.head())
print("\nMissing values:")
print(df.isna().sum())

X = df[["StudyHours", "Attendance", "AssignmentsCompleted"]]
y = df["FinalScore"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
}
results = []
for name, model in models.items():
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    results.append({
        "Model": name,
        "MAE": mean_absolute_error(y_test, predicted),
        "MSE": mean_squared_error(y_test, predicted),
        "R2": r2_score(y_test, predicted),
    })

comparison = pd.DataFrame(results).sort_values("MAE")
print("\nModel comparison (lower MAE/MSE is better):")
print(comparison.to_string(index=False, float_format=lambda n: f"{n:.3f}"))
print("\nSelected model (lowest test MAE):", comparison.iloc[0]["Model"])
print("Note: Small synthetic data; this is a learning exercise, not a production estimate.")
