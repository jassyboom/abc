
import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv('IRIS.csv')

print("feature and types")
for col in df.columns:
    if df[col].dtype=="object":
        print(f"{col} -> Nominal")
    else:
        print(f"{col} -> Numeric")
        
numeric_columns=df.select_dtypes(include=['float64','int64']).columns
df[numeric_columns].hist(figsize=(10,8))
plt.suptitle("Histograms of Iris Dataset Features", fontsize=16)

plt.show()
