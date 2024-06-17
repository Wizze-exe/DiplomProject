import pyedflib
import numpy as np
from scipy.signal import butter, filtfilt


def read_bdf(file_path):
    with pyedflib.EdfReader(file_path) as f:
        n = f.signals_in_file
        signal_labels = f.getSignalLabels()
        signals = np.array([f.readSignal(i) for i in range(n)])
    print(signal_labels, signals)
    return signal_labels, signals


def filter_signals(signals, low_cutoff, high_cutoff, fs):
    filtered_signals = np.array([bandpass_filter(signal, low_cutoff, high_cutoff, fs) for signal in signals])
    return filtered_signals


def bandpass_filter(signal, low_cutoff, high_cutoff, fs, order=5):
    """Применение бандпасс-фильтра Баттерворта к сигналу."""
    nyq = 0.5 * fs
    low = low_cutoff / nyq
    high = high_cutoff / nyq
    b, a = butter(order, [low, high], btype='band')
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal
