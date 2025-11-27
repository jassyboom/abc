import pandas as pd

df=pd.read_csv('IRIS.csv')
print("\n Dataset loaded succesfully ")
print(df.head())

species_list= ['Iris-setosa', 'Iris-versicolor', 'Iris-versico']

for species in species_list:
    print(f"\n statistical details for {species}") 
    
    species_df=df[df['species']==species] 
    
    stats=species_df.describe(percentiles=[0.25,0.5,0.75])
    
    print(stats)
              