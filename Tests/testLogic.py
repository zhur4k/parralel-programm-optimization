import unittest
from model.logic import Logic  # Импортируем ваш класс Logic


class TestLogic(unittest.TestCase):

    def setUp(self):
        self.logic = Logic()

    def test_generate_random_matrix(self):
        """Тест: Проверка генерации матрицы на симметричность и размер."""
        size = 5
        matrix = self.logic.generate_random_matrix(size)

        # Проверяем размер матрицы
        self.assertEqual(len(matrix), size)
        for row in matrix:
            self.assertEqual(len(row), size)

        # Проверяем симметричность матрицы
        for i in range(size):
            for j in range(size):
                self.assertEqual(matrix[i][j], matrix[j][i])

        # Проверяем, что диагональ заполнена нулями
        for i in range(size):
            self.assertEqual(matrix[i][i], 0)

    def test_tsp_branch_and_bound_small_graph(self):
        """Тест: Решение задачи коммивояжёра на маленьком графе."""
        graph = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ]
        best_tour, best_cost = self.logic.tsp_branch_and_bound(graph)

        # Ожидаемый результат: маршрут и его стоимость
        expected_cost = 80  # 0 -> 1 -> 3 -> 2 -> 0
        self.assertEqual(best_cost, expected_cost)
        self.assertEqual(set(best_tour), {0, 1, 2, 3})

    def test_tsp_branch_and_bound_random_matrix(self):
        """Тест: Решение задачи коммивояжёра на случайно сгенерированной матрице."""
        size = 4
        matrix = self.logic.generate_random_matrix(size)
        best_tour, best_cost = self.logic.tsp_branch_and_bound(matrix)

        # Проверяем корректность маршрута и стоимости
        self.assertEqual(len(best_tour), size)
        self.assertTrue(best_cost >= 0)

if __name__ == "__main__":
    unittest.main()
    