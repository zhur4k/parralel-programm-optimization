
import random


class Logic:

    def generate_random_matrix(self, size):
        """
        Генерация случайной симметричной матрицы конфликтов.
        :param size: Размер матрицы (количество узлов графа)
        :return: Матрица конфликтов
        """
        matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                if i == j:
                    row.append(0)
                elif j < i:  # Используем уже сгенерированное значение для симметрии
                    row.append(matrix[j][i])
                else:
                    row.append(random.randint(0, 1))  # Генерация 0 или 1 (конфликт или нет)
            matrix.append(row)
        return matrix

    def recursive_graph_coloring(self, graph, node_colors, node_index, num_colors):
        """
        Рекурсивный алгоритм оптимальной раскраски графа.

        :param graph: Список смежности графа
        :param node_colors: Текущая раскраска узлов
        :param node_index: Индекс текущего узла
        :param num_colors: Количество доступных цветов
        :return: True, если раскраска возможна, иначе False
        """
        if node_index == len(graph):
            return True

        for color in range(1, num_colors + 1):
            if self.is_safe_to_color(graph, node_colors, node_index, color):
                node_colors[node_index] = color
                if self.recursive_graph_coloring(graph, node_colors, node_index + 1, num_colors):
                    return True
                node_colors[node_index] = 0  # Отмена назначения цвета

        return False

    def is_safe_to_color(self, graph, node_colors, node_index, color):
        """
        Проверяет, можно ли безопасно раскрасить узел в заданный цвет.

        :param graph: Список смежности графа
        :param node_colors: Текущая раскраска узлов
        :param node_index: Индекс текущего узла
        :param color: Цвет для проверки
        :return: True, если узел можно покрасить, иначе False
        """
        for neighbor in graph[node_index]:
            if node_colors[neighbor] == color:
                return False
        return True

    def graph_coloring_optimization(self, conflict_matrix):
        """
        Оптимизация с использованием рекурсивной раскраски графов для минимизации ресурсов.

        :param conflict_matrix: Матрица смежности (конфликтов)
        :return: Количество ресурсов (процессоров/регистров) и раскраска узлов
        """
        # Преобразуем матрицу конфликтов в список смежности
        n = len(conflict_matrix)
        adjacency_list = {i: [] for i in range(n)}

        for i in range(n):
            for j in range(n):
                if conflict_matrix[i][j] == 1:
                    adjacency_list[i].append(j)

        # Определяем минимальное количество цветов через перебор
        for num_colors in range(1, n + 1):
            node_colors = [0] * n
            if self.recursive_graph_coloring(adjacency_list, node_colors, 0, num_colors):
                return num_colors, {i: node_colors[i] for i in range(n)}

        return n, {i: i for i in range(n)}  # Максимально возможная раскраска

    def optimize_parallel_program(self, conflict_matrix):
       
        num_resources, coloring = self.graph_coloring_optimization(conflict_matrix)

        print(f"Минимальное количество ресурсов (процессоров/регистров): {num_resources}")
        print(f"Раскраска узлов (задач): {coloring}")

        return num_resources, coloring