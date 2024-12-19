
import random


class Logic():

    def generate_random_matrix(self, size):
        matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                if i == j:
                    row.append(0)
                elif j < i:  # Используем уже сгенерированное значение для симметрии
                    row.append(matrix[j][i])
                else:
                    row.append(random.randint(1, 100))  # Генерация случайного числа от 1 до 100
            matrix.append(row)
        return matrix

    def tsp_branch_and_bound(self, graph):
        for row in graph:
            print(row)
        n = len(graph)
        all_nodes = set(range(n))
        best_tour = None
        best_cost = float('inf')

        def lower_bound(path):
            lb = 0
            for i in range(n):
                if i not in path:
                    lb += min(graph[i][j] for j in all_nodes - set(path))
            return lb

        def solve(node, path, cost):
            nonlocal best_tour, best_cost
            if len(path) == n:
                cost += graph[node][path[0]]
                if cost < best_cost:
                    best_tour = path
                    best_cost = cost
            else:
                for next_node in all_nodes - set(path):
                    new_cost = cost + graph[node][next_node]
                    if new_cost + lower_bound(path + [next_node]) < best_cost:
                        solve(next_node, path + [next_node], new_cost)

        solve(0, [0], 0)
        return best_tour, best_cost

