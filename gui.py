import traceback
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel
from data_processing import read_bdf, filter_signals
from statistics import calculate_mean, calculate_median, calculate_standard_deviation, calculate_power_spectrum
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class StatisticalModuleGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Statistical Module For BCI")
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.load_button = QPushButton("Load BDF file")
        layout.addWidget(self.load_button)
        self.load_button.clicked.connect(self.loadBDF)

        self.analyze_button = QPushButton("Analyze data")
        self.analyze_button.setEnabled(False)
        layout.addWidget(self.analyze_button)
        self.analyze_button.clicked.connect(self.analyzeData)

        self.results_label = QLabel("Analysis result:")
        layout.addWidget(self.results_label)

        self.plot_button = QPushButton("Plot data")
        self.plot_button.setEnabled(False)
        layout.addWidget(self.plot_button)
        self.plot_button.clicked.connect(self.plotPowerSpectrum)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def loadBDF(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open BDF file", "", "BDF Files (*.bdf)")
        if file_path:
            try:
                self.signal_labels, self.signals = read_bdf(file_path)
                if self.signals.size > 0:
                    self.analyze_button.setEnabled(True)
                    self.plot_button.setEnabled(True)
                else:
                    print("Ошибка: файл не содержит данных.")
            except Exception as e:
                print(f"Ошибка при загрузке файла: {e}")
                traceback.print_exc()
        else:
            print("Загрузка файла отменена пользователем.")

    def analyzeData(self):
        try:
            if not hasattr(self, 'signals') or self.signals.size == 0:
                print("Ошибка: данные сигналов не загружены")
                return

            signal = self.signals[0]
            mean = calculate_mean(signal)
            median = calculate_median(signal)
            std_dev = calculate_standard_deviation(signal)

            results_text = f"Mean: {mean}\nMedian: {median}\nStandard Deviation: {std_dev}"
            self.results_label.setText(results_text)

        except Exception as e:
            print(f"Произошла ошибка при анализе данных: {e}")
            traceback.print_exc()

    def plotPowerSpectrum(self):
        # Проверяем, есть ли данные сигналов
        if hasattr(self, 'signals') and self.signals is not None:
            # Очищаем предыдущий график, если он есть
            self.figure.clear()
            ax = self.figure.add_subplot(111)

            # Задаем параметры сэмплирования
            fs = 256  # или другое значение, соответствующее вашим данным

            # Рассчитываем спектральную мощность для первого сигнала в массиве
            signal = self.signals[0]
            freqs, power = calculate_power_spectrum(signal, fs)

            # Построение графика
            ax.plot(freqs, power)
            ax.set_title('Спектральная мощность сигнала')
            ax.set_xlabel('Частота (Гц)')
            ax.set_ylabel('Мощность')

            # Обновляем холст
            self.canvas.draw()
        else:
            print("Ошибка: данные сигналов не загружены для анализа.")
