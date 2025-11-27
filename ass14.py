import pandas as pd 

pd.set_option('display.float_format', '{:,.0f}'.format)

# Load Dataset
df = pd.read_csv('Covid Vaccine Statewise.csv')
print("\n Data loaded successfully")
print(df.head())

# A. Describe the dataset
print("\n Dataset Description")
print(df.describe(include='all'))

# B. Number of Males vaccinated
print("\n Total Number of Males Vaccinated")
male_vaccinated = df["Male(Individuals Vaccinated)"].sum()
print(male_vaccinated)

# C. Number of Females vaccinated
print("\n Total Number of Females Vaccinated")
female_vaccinated = df["Female(Individuals Vaccinated)"].sum()
print(female_vaccinated)


