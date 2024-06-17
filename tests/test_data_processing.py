import unittest

import numpy as np

from data_processing import read_bdf


class TestDataProcessing(unittest.TestCase):
    def test_read_bdf(self):
        # Проверяем, что функция read_bdf корректно считывает BDF файл
        # Для этого потребуется тестовый BDF файл
        signal_labels, signals = read_bdf('C:/Users\Timkh\PycharmProjects\DiplomProject/test.bdf')
        self.assertIsInstance(signal_labels, list)
        self.assertIsInstance(signals, np.ndarray)


if __name__ == '__main__':
    unittest.main()
