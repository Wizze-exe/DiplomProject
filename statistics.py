import numpy as np
from scipy import stats
from scipy.signal import welch


def calculate_mean(signal):
    """Вычисление среднего значения для каждого сигнала"""
    return np.mean(signal)


def calculate_median(signal):
    """Вычисление медианы для каждого сигнала"""
    return np.median(signal)


def calculate_standard_deviation(signal):
    """Вычисление стандартного отклонения для каждого сигнала"""
    return np.std(signal)


def calculate_power_spectrum(signal, fs):
    """Расчет спектральной мощности сигнала."""
    frequencies, power_spectrum = welch(signal, fs)
    return frequencies, power_spectrum


def perform_t_test(signal1, signal2):
    """Заполнение t-теста для двух наборов данных"""
    t_stat, p_value = stats.ttest_ind(signal1, signal2)
    return t_stat, p_value
