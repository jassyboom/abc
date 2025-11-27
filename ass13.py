import pandas as pd 

pd.set_option('display.float_format','{:,.0f}'.format)

df=pd.read_csv('Covid Vaccine Statewise.csv')
print("\n data loaded succesfully ")
print(df.head())

print("\n Dataset description")
print(df.describe(include='all'))

print("\n first dose vacination state wise ")
first_dose=df.groupby("state")["First Dose Administered"].sum()

print(first_dose)

print("\n second dose vaccination state wise ")
print("\n first dose vacination state wise ")
second_dose=df.groupby("state")["Second Dose Administered"].sum()

print(second_dose)

