import pandas as pd

df = pd.DataFrame({
    "StudyHours": [2, 4, 5, 7, 8, 6],
    "Attendance": [70, 75, 82, 90, 95, 88],
    "AssignmentsCompleted": [5, 6, 7, 9, 10, 8],
    "FinalScore": [55, 65, 72, 88, 94, 82]
})

# Independent variables used to make a prediction.
X = df[["StudyHours", "Attendance", "AssignmentsCompleted"]]

# Dependent variable we want to predict.
y = df["FinalScore"]

print("Features (X):")
print(X)

print("\nTarget (y):")
print(y)

print("\nFeature columns:", list(X.columns))
print("Target column:", y.name)
