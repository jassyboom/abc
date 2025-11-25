import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv(r"F:\TY SUBMISSION\DSML\DSML practical all assignment\Lipstick.csv",
                 encoding="utf-8-sig")

# Clean BOM from column names
df.columns = [c.replace("\ufeff", "") for c in df.columns]

print("Dataset Loaded Successfully\n")
print(df.head())

# Separate features & target
X = df.drop("Buys", axis=1)
y = df["Buys"]

# Encode all categorical columns
le_dict = {}
for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    le_dict[col] = le

# Encode target column
target_le = LabelEncoder()
y = target_le.fit_transform(y)

# Train decision tree
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

print("\nDecision Tree Model Trained Successfully!\n")

# ---- TEST DATA FOR QUESTION 6 ----
test_data = {
    "Id": [1],   # dummy ID
    "Age": [">35"],
    "Income": ["Medium"],
    "Gender": ["Female"],
    "Ms": ["Married"]
}

test_df = pd.DataFrame(test_data)

# Apply same encoders to test data
for col in test_df.columns:
    test_df[col] = le_dict[col].transform(test_df[col])

# Predict
prediction = model.predict(test_df)[0]
final_result = target_le.inverse_transform([prediction])[0]

print("Prediction for test data:")
print(test_data)

print("\nDecision: Customer will", final_result, "lipstick.")
