# import pandas as pd
# import matplotlib.pyplot as plt

# # Load dataset
# df = pd.read_csv(r"F:\TY SUBMISSION\DSML\DSML practical all assignment\IRIS.csv")

# print("Dataset Loaded Successfully!\n")
# print(df.head())

# # --------------------------------------------
# # 1. Create Boxplots for each feature
# # --------------------------------------------

# numeric_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

# plt.figure(figsize=(10, 6))
# df.boxplot(column=numeric_cols)
# plt.title("Box Plot of Iris Dataset Features")
# plt.ylabel("Value")
# plt.show()

# # --------------------------------------------
# # 2. Identify Outliers using IQR Method
# # --------------------------------------------

# print("\n========== OUTLIER DETECTION ==========\n")

# for col in numeric_cols:
#     Q1 = df[col].quantile(0.25)
#     Q3 = df[col].quantile(0.75)
#     IQR = Q3 - Q1

#     lower_limit = Q1 - 1.5 * IQR
#     upper_limit = Q3 + 1.5 * IQR

#     outliers = df[(df[col] < lower_limit) | (df[col] > upper_limit)][col]

#     print(f"Feature: {col}")
#     print(f" - Lower Bound: {lower_limit:.2f}")
#     print(f" - Upper Bound: {upper_limit:.2f}")

#     if len(outliers) == 0:
#         print(" - Outliers: None\n")
#     else:
#         print(f" - Outliers: {outliers.values}\n")

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('IRIS.csv')
print("Data loaded succesfully")
print(df.head())

numeric_column=["sepal_length", "sepal_width", "petal_length", "petal_width"]

plt.figure(figsize=(10,6))
df.boxplot(column=numeric_column)
plt.title("box plot of iris dataset")

plt.show()

print("\noutlier detection")

for col in numeric_column:
    Q1=df[col].quantile(0.25)
    Q3=df[col].quantile(0.75)
    IQR=Q3-Q1
    
    lower_limit=Q1-1.5*IQR
    upper_limit=Q3+1.5*IQR
    
    
    
    outliers=df[(df[col]<lower_limit)|(df[col]>upper_limit)][col]
    print(f"feature: {col}")
    print(f"lower bound: {lower_limit:.2f}")
    print(f"upper bound: {upper_limit:.2f}")
    
    if len(outliers)==0:
        print("-Outlier none \n")
    else:
        print(f"outlier:{list(outliers.values)}\n")