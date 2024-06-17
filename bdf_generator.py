import numpy as np
import pyedflib


def create_test_bdf(file_name, duration_sec=10, sample_rate=256):
    """Создает тестовый BDF-файл с рандомными данными."""
    n_channels = 2  # Количество каналов
    n_samples = duration_sec * sample_rate

    # Генерация случайных данных
    signal_data = np.random.rand(n_channels, n_samples) * 100

    # Создание нового BDF-файла
    with pyedflib.EdfWriter(file_name, n_channels=n_channels, file_type=pyedflib.FILETYPE_BDF) as writer:
        # Задаем информацию о каналах
        channel_info = []
        for i in range(n_channels):
            ch_dict = {'label': f'Ch{i}', 'dimension': 'uV', 'sample_rate': sample_rate, 'physical_min': 0,
                       'physical_max': 100, 'digital_min': -32768, 'digital_max': 32767}
            channel_info.append(ch_dict)

        writer.setSignalHeaders(channel_info)

        # Запись данных в файл
        for i in range(n_channels):
            writer.writePhysicalSamples(signal_data[i])

    print(f"Тестовый BDF-файл '{file_name}' успешно создан.")


# Использование функции для создания тестового файла
create_test_bdf('test.bdf')
