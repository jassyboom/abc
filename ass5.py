# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.tree import DecisionTreeClassifier

# # Load dataset
# df = pd.read_csv(r"F:\TY SUBMISSION\DSML\DSML practical all assignment\Lipstick.csv",
#                  encoding="utf-8-sig")

# # Remove BOM from column names if present
# df.columns = [c.replace("\ufeff", "") for c in df.columns]

# print("Dataset Loaded Successfully\n")
# print(df.head())

# # Separate features and target
# X = df.drop("Buys", axis=1)
# y = df["Buys"]

# # Encode categorical features
# le_dict = {}
# for col in X.columns:
#     le = LabelEncoder()
#     X[col] = le.fit_transform(X[col])
#     le_dict[col] = le

# # Encode target column
# target_le = LabelEncoder()
# y = target_le.fit_transform(y)

# # Train Decision Tree
# model = DecisionTreeClassifier(criterion="entropy")
# model.fit(X, y)

# print("\nDecision Tree Model Trained Successfully!\n")

# # ===== TEST DATA GIVEN IN QUESTION =====
# test_data = {
#     "Id": [1], 
#     "Age": ["<21"],
#     "Income": ["Low"],
#     "Gender": ["Female"],
#     "Ms": ["Married"]
# }

# test_df = pd.DataFrame(test_data)

# # Encode test data
# for col in test_df.columns:
#     test_df[col] = le_dict[col].transform(test_df[col])

# # Predict
# prediction = model.predict(test_df)[0]
# final_result = target_le.inverse_transform([prediction])[0]

# print("Prediction for test data:")
# print(test_data)

# # NO EMOJIS (Windows console cannot print them)
# print("\nDecision: Customer will", final_result, "lipstick.")

import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

df=pd.read_csv('Lipstick.csv',encoding="utf-8-sig")
df.columns=[c.replace("\ufeff","") for c in df.columns]

print("Dataset loaded Succesfully")
print(df.head())

X=df.drop("Buys",axis=1)
y=df["Buys"]

le_dict={}
for col in X.columns:
    le=LabelEncoder()
    X[col]=le.fit_transform(X[col])
    le_dict[col]=le
target_le=LabelEncoder()
y=target_le.fit_transform(y)

model=DecisionTreeClassifier(criterion="entropy")
model.fit(X,y)

print("\n Decison tree model trained succesfully ")
test_data={
    "Id":[1],
    "Age":["<21"],
    "Income":["Low"],
    "Gender":["Female"],
    "Ms":["Married"]
}
test_df=pd.DataFrame(test_data)

for col in test_df.columns:
    test_df[col]=le_dict[col].transform(test_df[col])
    
prediction=model.predict(test_df)[0]
final_result=target_le.inverse_transform([prediction])[0]

print("prediction for test data: ")
print(test_data)

print("\n Decison customer will ", final_result, "lipstick")

F:\TY SUBMISSION\DSML\DSML practical all assignment\ass5.py