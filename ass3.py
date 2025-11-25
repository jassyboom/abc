import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv('House Data.csv')
print("\n data loaded succesfully ")
print(df.head())

print("\n summary statistics of each feature")

for col in df.columns:
    print(f"\n feature: {col}")
    try:
        print("std deviation ", df[col].std())
    except:
        print("std deviation not applicable ")
    try:
        print("var", df[col].var())
    except:
        print("variance is not applicable ")
        
    try:
        print("25th percentile: ",df[col].quantile(0.25))
        print("50th percentile: ",df[col].quantile(0.50))
        print("75th percentile: ",df[col].quantile(0.75))
    except:
        print("percentile not applicable")
          
# ---------- HISTOGRAMS FOR ALL FEATURES ----------

print("\n===== HISTOGRAMS FOR ALL FEATURES =====")
# df.hist(figsize=(15, 10))
# plt.tight_layout()
# plt.show()
df.hist(figsize=(15,10))
plt.tight_layout()
plt.show()