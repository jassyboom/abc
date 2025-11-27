import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load Titanic Dataset

file_path = r"F:\TY SUBMISSION\DSML\DSML practical all assignment\Titanic.csv"
df = pd.read_csv(file_path)

print("Titanic Dataset Loaded Successfully!\n")
print(df.head())


# Basic Informatiob
print("\n===== Dataset Information =====\n")
print(df.info())

print("\n===== Dataset Description =====\n")
print(df.describe(include='all'))


# 1. Countplot: Survived vs Not Survived
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Survived", palette="Set2")
plt.title("Survival Count")
plt.show()


# 2. Survival by Gender

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Sex", hue="Survived", palette="Set1")
plt.title("Survival Based on Gender")
plt.show()


# 3. Survival by Passenger Class (Pclass)

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Pclass", hue="Survived", palette="Set3")
plt.title("Survival Based on Passenger Class")
plt.show()

# --------------------------------------
# 4. Age Distribution
# --------------------------------------
plt.figure(figsize=(8,4))
sns.histplot(df["Age"].dropna(), kde=True)
plt.title("Age Distribution")
plt.show()

# --------------------------------------
# 5. Boxplot of Age vs Survival
# --------------------------------------
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="Survived", y="Age")
plt.title("Age vs Survival")
plt.show()


# 6. Heatmap of Correlation
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

print("\nAnalysis Complete: Charts Displayed Successfully!")

