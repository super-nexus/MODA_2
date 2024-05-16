import csv
import random

# Parameters
num_nodes = 15
max_distance = 500  # maximum distance in meters between nodes
max_score = 5  # maximum score for scenic beauty, roughness, safety, and slope

# Initialize data structures
data = []

# Generate data
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        dij = random.randint(1, max_distance)
        aij = random.randint(1, max_score)
        bij = random.randint(1, max_score)
        sij = random.randint(1, max_score)
        lij = random.randint(1, max_score)
        data.append([i, j, dij, aij, bij, sij, lij])

# Save data to CSV
with open('bicycle_network.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["node1", "node2", "distance", "scenic_beauty", "roughness", "safety", "slope"])
    writer.writerows(data)

print("Data has been saved to bicycle_network.csv")

