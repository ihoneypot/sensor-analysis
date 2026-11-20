import sys
from PyQt6.QtWidgets import QApplication
from ui.dataAnalysis import Ui_MainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Sensor Analysis")
    window = Ui_MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
