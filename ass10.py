import numpy as np
from sklearn.cluster import KMeans

# Given Points
points = np.array([
    [2,10],  # P1
    [2,5],   # P2
    [8,4],   # P3
    [5,8],   # P4
    [7,5],   # P5
    [6,4],   # P6
    [1,2],   # P7
    [4,9]    # P8
])

# Initial Centroids: m1=P1, m2=P4, m3=P7
initial_centroids = np.array([
    [2,10],  # m1 = P1
    [5,8],   # m2 = P4
    [1,2]    # m3 = P7
])

# Create KMeans model
kmeans = KMeans(
    n_clusters=3,
    init=initial_centroids,
    n_init=1
)

# Fit the model
kmeans.fit(points)

# Print cluster labels for each point
labels = kmeans.labels_
print("Cluster assignments (P1 to P8):")
print(labels)

# 1] Which cluster does P6 belong to?
print("\n1] P6 belongs to Cluster:", labels[5])

# 2] Population of cluster around m3
population_m3 = list(labels).count(2)     # cluster index 2 = m3
print("2] Population of cluster around m3:", population_m3)

# 3] Updated centroids
print("\n3] Updated Centroids (m1, m2, m3):")
print(kmeans.cluster_centers_)
