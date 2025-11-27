import pandas as pd

# Load dataset
file_path = r"F:\TY SUBMISSION\DSML\DSML practical all assignment\Train Travel.csv"
df = pd.read_csv(file_path, encoding='utf-8-sig')

print("First 5 rows:\n", df.head(), "\n")

# Count unique values
print("Unique values in each column:\n", df.nunique(), "\n")

# Check data types
print("Data types:\n", df.dtypes, "\n")

# Identify missing values
print("Missing values before filling:\n", df.isnull().sum(), "\n")

# Fill missing values first
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col].fillna(df[col].mean(), inplace=True)  # numeric -> mean
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)  # categorical -> mode

print("Missing values after filling:\n", df.isnull().sum(), "\n")

# Convert data types safely
for col in df.columns:
    if df[col].dtype == 'int64':
        df[col] = df[col].astype('float')  # int -> float
    elif df[col].dtype == 'float64':
        # Convert to int only if it makes sense (e.g., columns like 'Age' or 'SibSp')
        if df[col].apply(float.is_integer).all():  # check all values are whole numbers
            df[col] = df[col].astype('int')
    elif df[col].dtype == 'object':
        df[col] = df[col].astype('category')  # object -> category

print("Data types after conversion:\n", df.dtypes, "\n")

# Final dataset info
print("Final dataset info:\n")
print(df.info())
