import unittest
import numpy as np
from statistics import calculate_mean, calculate_median, calculate_standard_deviation


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # Мы создадим тестовый набор данных для анализа
        self.test_data = np.array([1, 2, 3, 4, 5])

    def test_calculate_mean(self):
        # Проверка вычисления среднего значения
        self.assertEqual(calculate_mean(self.test_data), np.mean(self.test_data))

    def test_calculate_median(self):
        # Проверка вычисления медианы
        self.assertEqual(calculate_median(self.test_data), np.median(self.test_data))

    def test_calculate_standard_deviation(self):
        # Проверка вычисления стандартного отклонения
        self.assertEqual(calculate_standard_deviation(self.test_data), np.std(self.test_data))


if __name__ == '__main__':
    unittest.main()
