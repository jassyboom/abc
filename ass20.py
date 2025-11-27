import random 
import math
import pandas as pd

df=pd.read_csv('IRIS.csv')
data=df.iloc[:,0:4].values

def distance(p,q):
    return math.sqrt(sum((p[i]-q[i])**2 for i in range(len(p))))

random_indices=random.sample(range(len(data)),3)
m1=data[random_indices[0]]
m2=data[random_indices[1]]
m3=data[random_indices[2]]

print("Initial Random Centroids:")
print("Centroid 1:", m1)
print("Centroid 2:", m2)
print("Centroid 3:", m3)
print()

for iteration in range(10):
    c1,c2,c3=[],[],[]
    
    for point in data:
        d1=distance(point,m1)
        d2=distance(point,m2)
        d3=distance(point,m3)
        
        minimum=min(d1,d2,d3)
        
        if minimum==d1:
            c1.append(point)
        elif minimum==d2:
            c2.append(point)
        else:
            c3.append(point)
            
        def compute_centroid(cluster):
            return [sum(col)/len(col) for col in zip(*cluster)]
        
        m1=compute_centroid(c1)
        m2=compute_centroid(c2)
        m3=compute_centroid(c3)
        print(f"iteration {iteration+1} completed")
print("\nFinal Cluster Means (Centroids):")
print("Centroid 1:", m1)
print("Centroid 2:", m2)
print("Centroid 3:", m3)