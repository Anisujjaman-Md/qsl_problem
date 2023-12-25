import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

locations = np.array([
    (23.8728568, 90.3984184),  # Uttara Branch
    (23.8513998, 90.3944536),  # City Bank Airport
    (23.8330429, 90.4092871),  # City Bank Nikunja
    (23.8679743, 90.3840879),  # City Bank Beside Uttara Diagnostic
    (23.8248293, 90.3551134),  # City Bank Mirpur 12
    (23.827149, 90.4106238),   # City Bank Le Meridien
    (23.8629078, 90.3816318),  # City Bank Shaheed Sarani
    (23.8673789, 90.429412),   # City Bank Narayanganj
    (23.8248938, 90.3549467),  # City Bank Pallabi
    (23.813316, 90.4147498)    # City Bank JFP
])

dist_matrix = cdist(locations, locations, metric='euclidean')


G = nx.Graph()
for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        G.add_edge(i, j, weight=dist_matrix[i, j])


tsp_path = nx.approximation.traveling_salesman_problem(G, cycle=True)


optimized_locations = locations[tsp_path]


plt.figure(figsize=(8, 6))
plt.plot(locations[:, 1], locations[:, 0], 'o', label='Original Order')
plt.plot(optimized_locations[:, 1], optimized_locations[:, 0], 'o-', label='Optimized Order')
plt.title('Optimized TSP Route')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()
