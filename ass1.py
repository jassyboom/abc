# # --------------------------------------
# # DSML Practical - Problem 1 (Titanic)
# # Simple Code for VS Code / Jupyter
# # --------------------------------------

# import pandas as pd

# # --------------------------------------
# # 1) READ DATA (CSV & XLSX)
# # --------------------------------------

# # Read CSV file
# titanic_csv = pd.read_csv("Titanic.csv")
# print("\n---- Data Loaded from CSV ----")
# print(titanic_csv.head())

# # If you have Excel file uncomment below:
# # titanic_xls = pd.read_excel("Titanic.xlsx")
# # print("\n---- Data Loaded from Excel ----")
# # print(titanic_xls.head())


# # --------------------------------------
# # 2) INDEXING & SELECTING DATA
# # --------------------------------------

# print("\n---- Selecting First 5 Rows ----")
# print(titanic_csv.head())

# print("\n---- Selecting 'Name' and 'Age' Columns ----")
# print(titanic_csv[['Name', 'Age']].head())

# print("\n---- Selecting a Specific Row (Index 10) ----")
# print(titanic_csv.loc[10])


# # --------------------------------------
# # 3) SORTING DATA
# # --------------------------------------

# print("\n---- Sorting by Age ----")
# sorted_age = titanic_csv.sort_values(by='Age')
# print(sorted_age.head())

# print("\n---- Sorting by Fare (Descending) ----")
# sorted_fare = titanic_csv.sort_values(by='Fare', ascending=False)
# print(sorted_fare.head())


# # --------------------------------------
# # 4) DESCRIBE ATTRIBUTES
# # --------------------------------------

# print("\n---- Dataset Summary (describe()) ----")
# print(titanic_csv.describe(include='all'))


# # --------------------------------------
# # 5) CHECK DATA TYPES
# # --------------------------------------

# print("\n---- Data Types of Each Column ----")
# print(titanic_csv.dtypes)


# import pandas as pd

# titanic_csv=pd.read_csv("Titanic.csv")
# print("\n  data laoded succesully ")
# print(titanic_csv.head())

# print("\n selecting first five row ")
# print(titanic_csv.head())

# print("\n Selecting 'Name' and 'Age' Columns")
# print(titanic_csv[['Name','Age']].head())

# print("\n selection on specific location index 10") 
# print(titanic_csv.loc[10])   

# print("\n sort the data")
# sorted_age=titanic_csv.sort_values(by='Age')
# print(sorted_age.head())

# print("\n sort ascending order fare column ")
# sorted_fare=titanic_csv.sort_values(by='Fare', ascending=False)
# print(sorted_fare.head())

# print("\n dataset summary")
# print(titanic_csv.describe(include='all'))

# print("\n data types of each column")
# print(titanic_csv.dtypes)

import pandas as pd 

titanic_csv=pd.read_csv('Titanic.csv')

print("\n data loaded succesfully ")
print(titanic_csv.head())

# print("\n using xls")
# titanic_xls=pd.read_xls('Titanic.xls')
# print(titanic_xls.head())

print('\n Selecting name and age column ')
print(titanic_csv[['Name', 'Age']].head())

print('\n selecting at 10 th row ')
print(titanic_csv.loc[10])

print('\n sort the data')
sorted_age=titanic_csv.sort_values(by='Age')
print(sorted_age.head())

print("\n sort the data fare column by ascending order ")
sorted_fare=titanic_csv.sort_values(by='Fare', ascending=True)
print(sorted_fare.head())

print("\n describe all the data summary ")
print(titanic_csv.describe(include='all'))

print("\n titanic csv all column dtyped")
print(titanic_csv.dtypes)