import random

# Distance Matrix
distance_matrix = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

num_cities = len(distance_matrix)
population_size = 6
generations = 100
mutation_rate = 0.2


# Population Function
def create_population(size, cities):
    population = []
    for _ in range(size):
        route = random.sample(range(cities), cities)
        population.append(route)
    return population


# Fitness Function
def fitness(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += distance_matrix[route[i]][route[i + 1]]
    distance += distance_matrix[route[-1]][route[0]]
    return 1 / (distance + 1)


# Selection Function 
def selection(population):
    population.sort(key=lambda r: fitness(r), reverse=True)
    return population[:2]


# Crossover
def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1) - 2)
    child = parent1[:cut] + \
        [city for city in parent2 if city not in parent1[:cut]]
    return child


# Mutation 
def mutation(route):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route


# Replacement Function
def replacement(population, offspring):
    population.sort(key=lambda r: fitness(r))
    for i in range(len(offspring)):
        population[i] = offspring[i]
    return population


# Main Genetic Algorithm
population = create_population(population_size, num_cities)

for gen in range(generations):
    parents = selection(population)
    offspring = []
    for _ in range(population_size // 2):
        p1, p2 = random.sample(parents, 2)
        child1 = mutation(crossover(p1, p2))
        child2 = mutation(crossover(p2, p1))
        offspring.extend([child1, child2])
    population = replacement(population, offspring)

# Output
best_route = max(population, key=lambda r: fitness(r))
best_distance = 1 / fitness(best_route) - 1

print("Optimal Route:", best_route)
print("Minimum Distance:", best_distance)
