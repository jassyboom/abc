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
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

print("\nEncoded Data:")
print(df.head())

# -----------------------------
# 3. Split into features & target
# -----------------------------
# Target column is "Buys", not "Buy"
X = df.drop("Buys", axis=1)      # Features
y = df["Buys"]                   # Target

# -----------------------------
# 4. Train Decision Tree
# -----------------------------
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

print("\nDecision Tree Model Trained Successfully!")

# -----------------------------
# 5. Prepare Test Data
# Test case:
# [Age > 35, Income = Medium, Gender = Female, Marital Status = Married]
# Your CSV uses column names: Age, Income, Gender, Ms
# -----------------------------

test = pd.DataFrame({
    "Id": [1],
    "Age": [">35"],
    "Income": ["Medium"],
    "Gender": ["Female"],
    "Ms": ["Married"]
})

# Encode using LabelEncoder
for col in test.columns:
    test[col] = le.fit_transform(test[col])

print("\nEncoded Test Input:")
print(test)

# -----------------------------
# 6. Prediction
# -----------------------------
prediction = model.predict(test)
result = "Yes (Will Buy)" if prediction[0] == 1 else "No (Will Not Buy)"

print("\nFinal Prediction for Test Case:")
print(result)

# -----------------------------
# 7. OPTIONAL: View the Decision Tree
# -----------------------------
tree.plot_tree(model, filled=True)
