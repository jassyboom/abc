import pandas as pd
import random
import math

# Load dataset (only numeric columns)
df = pd.read_csv("IRIS.csv")
data = df.iloc[:, 0:4].values     # taking 4 numeric attributes

# Euclidean distance function
def distance(p, q):
    return math.sqrt(sum((p[i] - q[i]) ** 2 for i in range(len(p))))

# Randomly choose 4 initial centroids
random_indices = random.sample(range(len(data)), 4)
m1 = data[random_indices[0]]
m2 = data[random_indices[1]]
m3 = data[random_indices[2]]
m4 = data[random_indices[3]]

print("Initial Random Centroids:")
print("Centroid 1:", m1)
print("Centroid 2:", m2)
print("Centroid 3:", m3)
print("Centroid 4:", m4)
print()

# ---- Perform K-Means for 10 iterations ----
for iteration in range(10):

    c1, c2, c3, c4 = [], [], [], []

    # Assign each point to nearest centroid
    for point in data:
        d1 = distance(point, m1)
        d2 = distance(point, m2)
        d3 = distance(point, m3)
        d4 = distance(point, m4)

        minimum = min(d1, d2, d3, d4)

        if minimum == d1:
            c1.append(point)
        elif minimum == d2:
            c2.append(point)
        elif minimum == d3:
            c3.append(point)
        else:
            c4.append(point)

    # Function to compute new centroid
    def compute_centroid(cluster):
        return [sum(col) / len(col) for col in zip(*cluster)] if cluster else [0,0,0,0]

    # Update centroids
    m1 = compute_centroid(c1)
    m2 = compute_centroid(c2)
    m3 = compute_centroid(c3)
    m4 = compute_centroid(c4)

    print(f"Iteration {iteration+1} completed.")

# ---- Final Output ----
print("\nFinal Cluster Means (Centroids) after 10 iterations:")
print("Centroid 1:", m1)
print("Centroid 2:", m2)
print("Centroid 3:", m3)
print("Centroid 4:", m4)
