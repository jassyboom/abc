import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# -----------------------------
# 1. Load dataset
# -----------------------------
file_path = r"F:\TY SUBMISSION\DSML\DSML practical all assignment\Lipstick.csv"
df = pd.read_csv(file_path)

print("Dataset Loaded Successfully!")
print(df.head())

# -----------------------------
# 2. Encode categorical columns
# -----------------------------
encoders = {}

for col in df.columns:
    if df[col].dtype == object:     # only encode categorical columns
        encoders[col] = LabelEncoder()
        df[col] = encoders[col].fit_transform(df[col])

print("\nEncoded Data:")
print(df)

# -----------------------------
# 3. Split into features and target
# -----------------------------
X = df.drop("Buys", axis=1)
y = df["Buys"]

# -----------------------------
# 4. Train Decision Tree
# -----------------------------
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

print("\nDecision Tree Model Trained Successfully!")

# -----------------------------
# 5. Test Case (Q8)
# -----------------------------
test = pd.DataFrame({
    "Id": [1],
    "Age": ["21-35"],
    "Income": ["Low"],
    "Gender": ["Male"],
    "Ms": ["Married"]
})

# Encode only categorical columns (NOT Id)
for col in test.columns:
    if col in encoders:  # only encode if encoder exists
        test[col] = encoders[col].transform(test[col])

print("\nEncoded Test Input:")
print(test)

# -----------------------------
# 6. Predict
# -----------------------------
prediction = model.predict(test)[0]
result = "Yes (Customer WILL buy lipstick)" if prediction == 1 else "No (Customer will NOT buy lipstick)"

print("\nFinal Prediction for Test Case:")
print(result)

# -----------------------------
# 7. OPTIONAL: View Decision Tree
# -----------------------------
tree.plot_tree(model, filled=True)
