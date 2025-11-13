import random
import matplotlib.pyplot as plt
#Graph (Distance Matrix)
graph = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]
num_nodes = len(graph)
num_ants = 5
alpha = 1
beta = 2
evaporation = 0.3
iterations = 10
# Initialize pheromone
pheromone = [[1 for _ in range(num_nodes)] for _ in range(num_nodes)]
def path_cost(path):
    cost = 0
    for i in range(len(path)-1):
        cost += graph[path[i]][path[i+1]]
    return cost
def choose_next_node(current, visited):
    probs, total = [], 0
    for j in range(num_nodes):
        if graph[current][j] > 0 and j not in visited:
            val = (pheromone[current][j] ** alpha) * \
                ((1 / graph[current][j]) ** beta)
            probs.append((j, val))
            total += val
    if total == 0:
        return None
    r = random.random()
    cumulative = 0
    for node, prob in probs:
        cumulative += prob / total
        if r <= cumulative:
            return node
    return probs[-1][0]
# Main ACO
best_costs = []
for iteration in range(iterations):
    all_paths = []
    for _ in range(num_ants):
        path = [0]
        while len(path) < num_nodes:
            next_node = choose_next_node(path[-1], path)
            if next_node is None:
                break
            path.append(next_node)
        all_paths.append(path)
    # Pheromone evaporation
    for i in range(num_nodes):
        for j in range(num_nodes):
            pheromone[i][j] *= (1 - evaporation)
    # Pheromone update based on path quality
    for path in all_paths:
        cost = path_cost(path)
        if cost > 0:
            deposit = 1 / cost
            for k in range(len(path) - 1):
                a, b = path[k], path[k + 1]
                pheromone[a][b] += deposit
                pheromone[b][a] += deposit
    best_path = min(all_paths, key=path_cost)
    best_cost = path_cost(best_path)
    best_costs.append(best_cost)
    print(
        f"Iteration {iteration+1}: Best Path {best_path} | Cost = {best_cost}")
# Convergence Plot
plt.plot(best_costs, marker='o')
plt.title('ACO Convergence over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Best Path Cost')
plt.grid(True)
plt.show()
