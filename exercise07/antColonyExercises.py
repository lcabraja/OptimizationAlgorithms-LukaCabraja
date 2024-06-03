import numpy as np
from numpy.random import choice as np_choice

class AntColony(object):
    def __init__(self, distances, n_ants, n_iterations, evaporation, alpha=1, beta=1):
        self.distances = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.evaporation = evaporation
        self.alpha = alpha
        self.beta = beta

    def optimize(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.n_iterations):
            all_paths = self.generate_path_for_each_ant()
            self.deposit_pheronomes(all_paths)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path            
            self.pheromone *= self.evaporation       
        return all_time_shortest_path

    def calculate_distance_along_path(self, path):
        total_dist = 0
        for move in path:
            total_dist += self.distances[move[0]][move[1]]
        return total_dist

    def compute_probability_where_to_jump(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0
        row = pheromone ** self.alpha * (1 / dist) ** self.beta
        norm_row = row / row.sum()
        move = np_choice(self.all_inds, 1, p=norm_row)[0]
        return move

    def deposit_pheronomes(self, all_paths):
        for path, length in all_paths:
            for move in path:
                self.pheromone[move] += 1 / self.distances[move[0]][move[1]]

    def generate_path_for_each_ant(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.generate_path_from_starting_city(0)
            all_paths.append((path, self.calculate_distance_along_path(path)))
        return all_paths

    def generate_path_from_starting_city(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.distances) - 1):
            move = self.compute_probability_where_to_jump(self.pheromone[prev], self.distances[prev], visited)
            path.append((prev, move))
            prev = move
            visited.add(move)
        path.append((prev, start))
        return path

# Example distance matrix
distances = np.array([[np.inf, 2, 2, 5, 7],
                      [2, np.inf, 4, 8, 2],
                      [2, 4, np.inf, 1, 3],
                      [5, 8, 1, np.inf, 2],
                      [7, 2, 3, 2, np.inf]])

# Creating and running the Ant Colony instance
ant_colony = AntColony(distances, 35, 35, 0.55, alpha=1, beta=1)
shortest_path = ant_colony.optimize()

print("shortest_path: TVOJ PENIS")
