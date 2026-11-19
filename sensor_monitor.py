from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtWidgets import QGridLayout
import sys

from ui.dataAnalysis import Ui_MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Sensor Analysis")
    # app.setStyle("Fusion")
    window = Ui_MainWindow()
    window.show()
    return app.exec()

    # app = QtWidgets.QApplication(sys.argv)
    # app.setApplicationName("Sensor Analysis")
    # # app.setStyle("Fusion")
    # window = build_ui()
    # window.show()
    # return app.exec()



if __name__ == "__main__":
    sys.exit(main())
