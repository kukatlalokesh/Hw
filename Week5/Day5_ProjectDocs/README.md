# Week 5 Friday — Student Performance Prediction

## Problem statement
Predict a student's final score from study hours, attendance, and assignments completed.

## Dataset
The project uses 30 **synthetic example records** in `Day5_MiniProject/students.csv`. These are made-up training examples for homework, not real student data.

## Preprocessing
Read the CSV with Pandas, inspect the first rows and missing values, select three numeric features and one target, then split 75% training / 25% testing with `random_state=42`. No missing values or categorical columns are present in this example.

## Models
- Linear Regression
- Random Forest Regressor (100 trees)

## Evaluation
Evaluate both models on the same held-out test set using MAE, MSE, and R². The script prints the measured scores and selects the model with the lowest test MAE; **the winner is not assumed in advance**. Lower MAE and MSE are better; higher R² is generally better.

## Conclusion
The comparison demonstrates an end-to-end regression workflow and how to choose between models using test metrics. Because the dataset is tiny and synthetic, scores may not generalize to real students.

## Run
From the repository root:
```bash
python -m pip install -r Week5/Day5_GitSummary/requirements.txt
python Week5/Day5_MiniProject/student_performance_prediction.py
```
