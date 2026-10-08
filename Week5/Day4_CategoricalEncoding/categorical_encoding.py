import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

departments = pd.DataFrame({"Department": ["IT", "HR", "Finance", "IT", "HR"]})
label_encoder = LabelEncoder()
departments["LabelEncoded"] = label_encoder.fit_transform(departments["Department"])
print("Label encoding:")
print(departments)

one_hot_encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
encoded = one_hot_encoder.fit_transform(departments[["Department"]])
print("\nOne-hot encoded columns:", one_hot_encoder.get_feature_names_out())
print(encoded)
print("\nFor unordered categories, one-hot encoding avoids implying a numeric order.")
