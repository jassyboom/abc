import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load dataset
# file_path = r"F:\TY SUBMISSION\DSML\DSML practical all assignment\Train Travel.csv"
df = pd.read_csv('Train Travel.csv', encoding='utf-8-sig')

print("First 5 rows:\n", df.head(), "\n")

# ---------------------
# DATA CLEANING
# ---------------------

# 1. Remove duplicates
df.drop_duplicates(inplace=True)

# 2. Identify missing values
print("Missing values before cleaning:\n", df.isnull().sum(), "\n")

# 3. Fill missing values
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col].fillna(df[col].mean(), inplace=True)  # numeric -> mean
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)  # categorical -> mode

print("Missing values after filling:\n", df.isnull().sum(), "\n")

# ---------------------
# DATA TRANSFORMATION
# ---------------------

# 1. Convert object columns to category
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype('category')

# 2. Encode categorical variables using LabelEncoder
label_encoders = {}
for col in df.select_dtypes(include=['category']).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # save encoder if needed later

# 3. Normalize numeric columns (optional)
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# ---------------------
# FINAL DATA CHECK
# ---------------------
print("Data types after transformation:\n", df.dtypes, "\n")
print("First 5 rows after cleaning & transformation:\n", df.head(), "\n")
print("Dataset info:\n")
print(df.info())
