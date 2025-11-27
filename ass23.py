import pandas as pd
import math
from collections import Counter

# Step 1: Create the dataset
data = {
    "Age": ["Young","Young","Middle","Old","Old","Old","Middle","Young","Old","Young","Middle","Middle","Old"],
    "Income": ["High","High","High","Medium","Low","Low","Low","Medium","Medium","Medium","Medium","High","Medium"],
    "Married": ["No","No","No","No","Yes","Yes","Yes","No","Yes","Yes","No","Yes","No"],
    "Health": ["Fair","Good","Fair","Fair","Fair","Good","Good","Fair","Fair","Good","Good","Fair","Good"],
    "Class": ["No","No","Yes","Yes","Yes","No","Yes","No","Yes","Yes","Yes","Yes","No"]
}

df = pd.DataFrame(data)

# Step 2: Frequency table for Age
freq_table = pd.crosstab(df['Age'], df['Class'])
print("Frequency Table (Age vs Class):\n", freq_table)

# Step 3: Helper functions to calculate entropy
def entropy(labels):
    total = len(labels)
    counts = Counter(labels)
    ent = 0
    for c in counts.values():
        p = c / total
        if p > 0:
            ent -= p * math.log2(p)
    return ent

# Step 4: Calculate entropy of total dataset
total_entropy = entropy(df['Class'])
print("\nEntropy of Class:", total_entropy)

# Step 5: Calculate entropy for each Age group
age_groups = df.groupby('Age')
weighted_entropy = 0
for name, group in age_groups:
    group_entropy = entropy(group['Class'])
    weight = len(group) / len(df)
    weighted_entropy += weight * group_entropy
    print(f"Entropy for Age={name}: {group_entropy:.4f}, Weight: {weight:.4f}")

# Step 6: Information gain
info_gain = total_entropy - weighted_entropy
print("\nInformation Gain for Age:", info_gain)
