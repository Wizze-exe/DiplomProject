from PyQt5.QtWidgets import QApplication
from gui import StatisticalModuleGUI


def main():
    app = QApplication([])
    window = StatisticalModuleGUI()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
