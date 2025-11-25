# import pandas as pd

# Telecom_churn_csv=pd.read_csv('Telecom Churn.csv')
# print(Telecom_churn_csv.head())

# print(Telecom_churn_csv.columns)
# ------------------------------
# DSML Practical – Problem 2
# Telecom Churn Summary Statistics
# ------------------------------

# import pandas as pd

# # 👉 Load dataset (Change path according to your
# df=pd.read_csv('Telecom Churn.csv')

# print("\n===== DATASET LOADED SUCCESSFULLY =====\n")
# print(df.head())

# print("\n===== COLUMN NAMES =====")
# print(df.columns)
import pandas as pd

df=pd.read_csv('Telecom Churn.csv')
print("\n===== DATASET LOADED SUCCESSFULLY =====\n")
print(df.head())

print("\n===== COLUMN NAMES =====")
print(df.columns)
# 👉 Loop over each column and print statistics
print("\n===== SUMMARY STATISTICS FOR EACH FEATURE =====\n")

for col in df.columns:
    print(f"\n feature : {col} ")
    
    try:
        print("minimum:", df[col].min())
    except:
        print("minimum: not applicable ")
    
    try:
        print("maximum: ", df[col].max())
    except:
        print("Maximum not applicable ")
    try:
        print("me ",df[col].mean())
    except:
        print("Mean: not applicable ")
    try:
        print("Range : ", df[col].max()-df[col].min())
    except:
        print("Range: not applicable")
    try:
        print("std deviation :",df[col].std())
    except:
        print("std deviation is not applicable ")
    try:
        print("Variance:", df[col].var())
    except:
        print("Variance: Not applicable")
    try:
        print("25 th percentile",df[col].quantile(0.25))
        print("50 th percentile",df[col].quantile(0.50))
        print("75 th percentile",df[col].quantile(0.75))
    except:
        print("percentile not applicabel ")