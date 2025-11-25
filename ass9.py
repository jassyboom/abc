import math

# Points
points = {
    "P1": (0.1, 0.6),
    "P2": (0.15, 0.71),
    "P3": (0.08, 0.9),
    "P4": (0.16, 0.85),
    "P5": (0.2, 0.3),
    "P6": (0.25, 0.5),
    "P7": (0.24, 0.1),
    "P8": (0.3, 0.2)
}

# Initial centroids
m1 = points["P1"]  # C1
m2 = points["P8"]  # C2

def distance(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

C1 = []
C2 = []

# Assign each point to nearest centroid
for name, p in points.items():
    d1 = distance(p, m1)
    d2 = distance(p, m2)

    if d1 < d2:
        C1.append(name)
    else:
        C2.append(name)

# Function to compute new centroid
def compute_centroid(cluster):
    x = sum(points[p][0] for p in cluster) / len(cluster)
    y = sum(points[p][1] for p in cluster) / len(cluster)
    return (x, y)

new_m1 = compute_centroid(C1)
new_m2 = compute_centroid(C2)

# Output
print("Cluster 1:", C1)
print("Cluster 2:", C2)
print()

print("1) P6 belongs to:", "C1" if "P6" in C1 else "C2")
print("2) Population of cluster around m2:", len(C2))
print("3) Updated m1:", new_m1)
print("3) Updated m2:", new_m2)
