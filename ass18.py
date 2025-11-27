
import pandas as pd
df=pd.read_csv('House Data.csv')

print("Data loaded succesfully ")
print(df.head())

categorical_var=df.select_dtypes(include=['object']).columns
numerical_var=df.select_dtypes(include=['float64','int64']).columns

print("\n Categorical variable")
print(categorical_var)

print("\n numerical variable")
print(numerical_var)

categorical_column=categorical_var[0]

print(f"\n using cateforical variable for grouping :{categorical_column}")

grouped_summary=df.groupby(categorical_column)[numerical_var].agg(['mean','median','min','max','std'])

print("\n Summary statistics grouped by categorical variable ")
print(grouped_summary)