from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QRegularExpression

import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
ICO_FOLDER = f'{ROOT_PATH}/imgs/folder3.ico'
DOWNROW = f'{ROOT_PATH}/imgs/downrow.png'
RUN = f'{ROOT_PATH}/imgs/report.ico'
SAVE = f'{ROOT_PATH}/imgs/save.ico'
CLEAR = f'{ROOT_PATH}/imgs/clear.ico'

CUSTOM_WIDGET = ( 
    "QWidget{"
        "border-radius: 10px;"
        "background-color: rgb(46, 49, 70);"
    "}"
)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def set_label_stylesheet(self, font_size=15, padding_left=0):
        clabel = (
            "background-color: rgba(255, 255, 255, 0);"
            "color: rgb(236, 236, 236);"
            f"padding-left: {padding_left}px;"
            f"font-size: {font_size}pt;"
        )

        return clabel
    
    def custom_lineedit_stylesheet(self, background_color_rgb=(112, 112, 112)):
        clineedit = (
            "QLineEdit {"
                f"background-color: rgb{background_color_rgb};"
                "color: rgb(236, 236, 236);"
                "border: none;"
                "border-radius: 10px;"
                "padding: 4px 4px;"
                "height: 30px;"
            "}"
            "QLineEdit:focus {"
            "border-radius: 10px;"
            "}"
        )
        
        return clineedit
    
    def custom_combobox_stylesheet(self, background_color_rgb=(112, 112, 112)):
        ccombobox = (
            "QComboBox {"
                f"background-color: rgb{background_color_rgb};"
                "color: rgb(236, 236, 236);"
                "border: none;"
                "border-radius: 10px;"
                "min-height: 30px;"
                "padding-left: 10px;"
            "}"

            "QComboBox::drop-down {"
                "border: none;"
                "border-radius: 10px;"
            "}"

            "QComboBox QAbstractItemView {"
                "background-color: rgb(46, 49, 70);"
                "color: rgb(236, 236, 236);"
                "border: 1px solid rgb(88, 88, 88);"
                "border-radius: 10px;"
                "selection-background-color: rgb(88, 88, 88);"
                "outline: none;"
            "}"

            "QComboBox::down-arrow {"
                f"image: url({DOWNROW});"
                "width: 12px;"
                "height: 12px;"
                "margin-right: 15px;"
            "}"
        )
        return ccombobox
    
    def custom_pbutton_stylesheet(self, icon):
        cpbutton = (
            "QPushButton{\n"
                f"qproperty-icon: url({icon});"
                "qproperty-iconSize: 28px;"
                "background-color: rgb(112, 112, 112);\n"
                "border-radius: 10px;\n"
                "color: rgb(236, 236, 236);\n"
            "}\n"
            "QPushButton:hover{\n"
            "    background-color: rgb(88, 88, 88);\n"
            "}\n"
            "QPushButton:pressed{\n"
                "background-color: rgb(120, 120, 120);\n"
            "}"
        )
        return cpbutton

    def on_checkbox_checked(self):
        if self.wdg_datasel_checkBox_randomdata.isChecked():
            self.wdg_datasel_lineEdit_filepath.setEnabled(False)
            self.wdg_datasel_lineEdit_filepath.setStyleSheet(self.custom_lineedit_stylesheet(background_color_rgb=(80, 80, 80)))
            self.wdg_datasel_bt_OpenFile.setEnabled(False)
            self.wdg_datasel_comboBox_sensortype.setEnabled(True)
            self.wdg_datasel_comboBox_sensortype.setStyleSheet(self.custom_combobox_stylesheet())
            self.wdg_datasel_lineEdit_max.setEnabled(True)
            self.wdg_datasel_lineEdit_max.setStyleSheet(self.custom_lineedit_stylesheet())
            self.wdg_datasel_lineEdit_min.setEnabled(True)
            self.wdg_datasel_lineEdit_min.setStyleSheet(self.custom_lineedit_stylesheet())
        else:
            self.wdg_datasel_lineEdit_filepath.setEnabled(True)
            self.wdg_datasel_lineEdit_filepath.setStyleSheet(self.custom_lineedit_stylesheet())
            self.wdg_datasel_bt_OpenFile.setEnabled(True)
            self.wdg_datasel_comboBox_sensortype.setEnabled(False)
            self.wdg_datasel_comboBox_sensortype.setStyleSheet(self.custom_combobox_stylesheet(background_color_rgb=(80, 80, 80)))
            self.wdg_datasel_lineEdit_max.setEnabled(False)
            self.wdg_datasel_lineEdit_max.setStyleSheet(self.custom_lineedit_stylesheet(background_color_rgb=(80, 80, 80)))
            self.wdg_datasel_lineEdit_min.setEnabled(False)
            self.wdg_datasel_lineEdit_min.setStyleSheet(self.custom_lineedit_stylesheet(background_color_rgb=(80, 80, 80)))
    
    def show_error(self, title, error):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setWindowTitle("Warning")
        msg.setText(title)
        msg.setInformativeText(str(error))
        msg.exec()

    def setupUi(self):
        self.resize(820, 900)
        self.setWindowTitle("Data Analysis Tool")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("background-color: rgb(36, 36, 39);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        self.widget_main = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_main)
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_3.setSpacing(9)
        
        self.widget_dataselection = QtWidgets.QWidget(self.widget_main)
        self.widget_dataselection.setFixedSize(400, 390)
        self.widget_dataselection.setStyleSheet(CUSTOM_WIDGET)
        self.gridLayout = QtWidgets.QGridLayout(self.widget_dataselection)
        self.gridLayout.setContentsMargins(8, -1, -1, -1)

        self.wdg_datasel_checkBox_randomdata = QtWidgets.QCheckBox(self.widget_dataselection)
        self.wdg_datasel_checkBox_randomdata.setText('Random data')
        self.wdg_datasel_checkBox_randomdata.toggled.connect(self.on_checkbox_checked)
        self.gridLayout.addWidget(self.wdg_datasel_checkBox_randomdata, 0, 0, 1, 3)

        self.wdg_datasel_label_selectsensor = QtWidgets.QLabel(self.widget_dataselection)
        self.wdg_datasel_label_selectsensor.setStyleSheet(self.set_label_stylesheet())
        self.wdg_datasel_label_selectsensor.setText('Select sensor file')
        self.gridLayout.addWidget(self.wdg_datasel_label_selectsensor, 1, 0, 1, 3)
        
        self.wdg_datasel_bt_OpenFile = QtWidgets.QPushButton(self.widget_dataselection)
        self.wdg_datasel_bt_OpenFile.setStyleSheet(self.custom_pbutton_stylesheet(ICO_FOLDER))
        self.wdg_datasel_bt_OpenFile.setText('Open')
        self.wdg_datasel_bt_OpenFile.setFixedSize(80, 35)
        self.gridLayout.addWidget(self.wdg_datasel_bt_OpenFile, 2, 0, 1, 1)

        self.wdg_datasel_lineEdit_filepath = QtWidgets.QLineEdit(self.widget_dataselection)
        self.wdg_datasel_lineEdit_filepath.setStyleSheet(self.custom_lineedit_stylesheet())
        self.wdg_datasel_lineEdit_filepath.setPlaceholderText("C:\\Users\\")
        self.wdg_datasel_lineEdit_filepath.setFixedHeight(35)
        self.gridLayout.addWidget(self.wdg_datasel_lineEdit_filepath, 2, 1, 1, 2)

        self.wdg_datasel_label_sensortype = QtWidgets.QLabel(self.widget_dataselection)
        self.wdg_datasel_label_sensortype.setStyleSheet(self.set_label_stylesheet())
        self.wdg_datasel_label_sensortype.setText('Select sesnor type')
        self.gridLayout.addWidget(self.wdg_datasel_label_sensortype, 3, 0, 1, 3)

        self.wdg_datasel_comboBox_sensortype = QtWidgets.QComboBox(self.widget_dataselection)
        self.wdg_datasel_comboBox_sensortype.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
        self.wdg_datasel_comboBox_sensortype.setStyleSheet(self.custom_combobox_stylesheet(background_color_rgb=(80, 80, 80)))
        self.wdg_datasel_comboBox_sensortype.setMaxVisibleItems(5)

        self.wdg_datasel_comboBox_sensortype.addItems([
            "Temp sensor",
            "Humidity sensor",
            "Energy sensor"
        ])
        self.wdg_datasel_comboBox_sensortype.setEnabled(False)
        self.gridLayout.addWidget(self.wdg_datasel_comboBox_sensortype, 4, 0, 1, 3)

        self.wdg_datasel_label_numberofreadings = QtWidgets.QLabel(self.widget_dataselection)
        self.wdg_datasel_label_numberofreadings.setStyleSheet(self.set_label_stylesheet())
        self.wdg_datasel_label_numberofreadings.setText('Number of readings')
        self.gridLayout.addWidget(self.wdg_datasel_label_numberofreadings, 5, 0, 1, 2)

        self.wdg_datasel_lineEdit_numreadings = QtWidgets.QLineEdit(self.widget_dataselection)
        self.wdg_datasel_lineEdit_numreadings.setStyleSheet(self.custom_lineedit_stylesheet())
        self.wdg_datasel_lineEdit_numreadings.setPlaceholderText("100")
        self.wdg_datasel_lineEdit_numreadings.setValidator(QtGui.QIntValidator(-99999, 99999))
        self.wdg_datasel_lineEdit_numreadings.setMaximumSize(QtCore.QSize(50, 16777215))
        self.gridLayout.addWidget(self.wdg_datasel_lineEdit_numreadings, 5, 2, 1, 1)

        self.wdg_datasel_label_max = QtWidgets.QLabel(self.widget_dataselection)
        self.wdg_datasel_label_max.setStyleSheet(self.set_label_stylesheet())
        self.wdg_datasel_label_max.setText('Maximum')
        self.gridLayout.addWidget(self.wdg_datasel_label_max, 6, 0, 1, 1)

        self.wdg_datasel_lineEdit_max = QtWidgets.QLineEdit(self.widget_dataselection)
        self.wdg_datasel_lineEdit_max.setStyleSheet(self.custom_lineedit_stylesheet(background_color_rgb=(80, 80, 80)))
        self.wdg_datasel_lineEdit_max.setPlaceholderText("10.0")
        self.wdg_datasel_lineEdit_max.setMaximumSize(QtCore.QSize(50, 16777215))
        validator = QtGui.QDoubleValidator(-9999.0, 9999.0, 2)
        validator.setNotation(QtGui.QDoubleValidator.Notation.StandardNotation)
        validator.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English))
        self.wdg_datasel_lineEdit_max.setValidator(validator)
        self.wdg_datasel_lineEdit_max.setEnabled(False)
        self.gridLayout.addWidget(self.wdg_datasel_lineEdit_max, 6, 2, 1, 1)

        self.wdg_datasel_label_min = QtWidgets.QLabel(self.widget_dataselection)
        self.wdg_datasel_label_min.setStyleSheet(self.set_label_stylesheet())
        self.wdg_datasel_label_min.setText('Minimum')
        self.gridLayout.addWidget(self.wdg_datasel_label_min, 7, 0, 1, 1)

        self.wdg_datasel_lineEdit_min = QtWidgets.QLineEdit(self.widget_dataselection)
        self.wdg_datasel_lineEdit_min.setStyleSheet(self.custom_lineedit_stylesheet(background_color_rgb=(80, 80, 80)))
        self.wdg_datasel_lineEdit_min.setPlaceholderText("-2.0")
        self.wdg_datasel_lineEdit_min.setMaximumSize(QtCore.QSize(50, 16777215))
        validator = QtGui.QDoubleValidator(-99999.0, 99999.0, 2)
        validator.setNotation(QtGui.QDoubleValidator.Notation.StandardNotation)
        validator.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English))
        self.wdg_datasel_lineEdit_min.setValidator(validator)
        self.wdg_datasel_lineEdit_min.setEnabled(False)
        self.gridLayout.addWidget(self.wdg_datasel_lineEdit_min, 7, 2, 1, 1)

        self.wdg_datasel_label_alertthreshold = QtWidgets.QLabel(self.widget_dataselection)
        self.wdg_datasel_label_alertthreshold.setStyleSheet(self.set_label_stylesheet())
        self.wdg_datasel_label_alertthreshold.setText('Alert Threshold')
        self.gridLayout.addWidget(self.wdg_datasel_label_alertthreshold, 8, 0, 1, 2)

        self.wdg_datasel_lineEdit_alertthreashold = QtWidgets.QLineEdit(self.widget_dataselection)
        self.wdg_datasel_lineEdit_alertthreashold.setStyleSheet(self.custom_lineedit_stylesheet())
        self.wdg_datasel_lineEdit_alertthreashold.setPlaceholderText("7.0")
        self.wdg_datasel_lineEdit_alertthreashold.setMaximumSize(QtCore.QSize(50, 16777215))
        validator = QtGui.QDoubleValidator(-99999.0, 99999.0, 2)
        validator.setNotation(QtGui.QDoubleValidator.Notation.StandardNotation)
        validator.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English))
        self.wdg_datasel_lineEdit_alertthreashold.setValidator(validator)
        self.gridLayout.addWidget(self.wdg_datasel_lineEdit_alertthreashold, 8, 2, 1, 1)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(8)
        
        self.wdg_datasel_bt_apply = QtWidgets.QPushButton("Run")
        self.wdg_datasel_bt_apply.setStyleSheet(self.custom_pbutton_stylesheet(RUN))
        self.wdg_datasel_bt_apply.setFixedHeight(35)

        self.wdg_datasel_bt_save = QtWidgets.QPushButton("Save")
        self.wdg_datasel_bt_save.setStyleSheet(self.custom_pbutton_stylesheet(SAVE))
        self.wdg_datasel_bt_save.setFixedHeight(35)
        

        self.wdg_datasel_bt_clear = QtWidgets.QPushButton("Clear")
        self.wdg_datasel_bt_clear.setStyleSheet(self.custom_pbutton_stylesheet(CLEAR))
        self.wdg_datasel_bt_clear.setFixedHeight(35)

        button_layout.addWidget(self.wdg_datasel_bt_apply, 1)
        button_layout.addWidget(self.wdg_datasel_bt_save, 1)
        button_layout.addWidget(self.wdg_datasel_bt_clear, 1)

        self.gridLayout.addLayout(button_layout, 10, 0, 1, 3)
        self.gridLayout_3.addWidget(self.widget_dataselection, 0, 0, 1, 1)

        #############################################################
        self.widget_histogram = QtWidgets.QWidget(self.widget_main)
        self.widget_histogram.setFixedSize(390, 390)
        self.widget_histogram.setStyleSheet(CUSTOM_WIDGET)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_histogram)
        self.verticalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        
        self.label_showhistogram = QtWidgets.QLabel(self.widget_histogram)
        self.label_showhistogram.setText('Histogram')
        self.label_showhistogram.setStyleSheet(self.set_label_stylesheet(font_size=25))
        self.label_showhistogram.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_3.addWidget(self.label_showhistogram)

        #############################################################
        self.widget_plot = QtWidgets.QWidget(self.widget_main)
        self.widget_plot.setStyleSheet(CUSTOM_WIDGET)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_plot)
        self.verticalLayout_4.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        
        self.label_plot = QtWidgets.QLabel(self.widget_plot)
        self.label_plot.setText('Plot')
        self.label_plot.setStyleSheet(self.set_label_stylesheet(font_size=25))
        self.label_plot.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_4.addWidget(self.label_plot)
        
        self.gridLayout_3.addWidget(self.widget_histogram, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.widget_plot, 1, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.widget_main)
        
        self.setCentralWidget(self.centralwidget)
        
        #############################################################
        self.widget_calculatedreadings = QtWidgets.QWidget(self.widget_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_calculatedreadings.sizePolicy().hasHeightForWidth())
        self.widget_calculatedreadings.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_calculatedreadings)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(9)
        self.widget_mean = QtWidgets.QWidget(self.widget_calculatedreadings)
        self.widget_mean.setStyleSheet(CUSTOM_WIDGET)

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_mean)
        self.verticalLayout_6.setSpacing(0)
        
        self.label_mean = QtWidgets.QLabel(self.widget_mean)
        self.label_mean.setText('Mean')
        self.label_mean.setStyleSheet(self.set_label_stylesheet(padding_left=10))
        self.verticalLayout_6.addWidget(self.label_mean)
        
        self.label_int_mean = QtWidgets.QLabel(self.widget_mean)
        self.label_int_mean.setText('0')
        self.label_int_mean.setStyleSheet(self.set_label_stylesheet(font_size=25, padding_left=10))
        self.verticalLayout_6.addWidget(self.label_int_mean)
        
        self.widget_numreadings = QtWidgets.QWidget(self.widget_calculatedreadings)
        self.widget_numreadings.setStyleSheet(CUSTOM_WIDGET)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_numreadings)
        self.verticalLayout_5.setSpacing(0)
        
        self.label_readings = QtWidgets.QLabel(self.widget_numreadings)
        self.label_readings.setStyleSheet(self.set_label_stylesheet(padding_left=10))
        self.label_readings.setText('Readings')
        self.verticalLayout_5.addWidget(self.label_readings)

        self.label_int_numreadings = QtWidgets.QLabel(self.widget_numreadings)
        self.label_int_numreadings.setStyleSheet(self.set_label_stylesheet(font_size=25, padding_left=10))
        self.label_int_numreadings.setText('0')
        self.verticalLayout_5.addWidget(self.label_int_numreadings)
        
        self.widget_min = QtWidgets.QWidget(self.widget_calculatedreadings)
        self.widget_min.setStyleSheet(CUSTOM_WIDGET)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_min)
        self.verticalLayout_7.setSpacing(0)
        
        self.label_min = QtWidgets.QLabel(self.widget_min)
        self.label_min.setStyleSheet(self.set_label_stylesheet(padding_left=10))
        self.label_min.setText('Minimum')
        self.verticalLayout_7.addWidget(self.label_min)
        
        self.label_int_min = QtWidgets.QLabel(self.widget_min)
        self.label_int_min.setStyleSheet(self.set_label_stylesheet(font_size=25, padding_left=10))
        self.label_int_min.setText('0')
        self.verticalLayout_7.addWidget(self.label_int_min)
        
        self.widget_stddeviation = QtWidgets.QWidget(self.widget_calculatedreadings)
        self.widget_stddeviation.setStyleSheet(CUSTOM_WIDGET)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_stddeviation)
        self.verticalLayout_8.setSpacing(0)

        self.label_stddeviation = QtWidgets.QLabel(self.widget_stddeviation)
        self.label_stddeviation.setStyleSheet(self.set_label_stylesheet(padding_left=10))
        self.label_stddeviation.setText('Standard deviation')
        self.verticalLayout_8.addWidget(self.label_stddeviation)

        self.label_int_stddeviation = QtWidgets.QLabel(self.widget_stddeviation)
        self.label_int_stddeviation.setStyleSheet(self.set_label_stylesheet(font_size=25, padding_left=10))
        self.label_int_stddeviation.setText('0')
        self.verticalLayout_8.addWidget(self.label_int_stddeviation)
        
        self.widget_abovethreshold = QtWidgets.QWidget(self.widget_calculatedreadings)
        self.widget_abovethreshold.setStyleSheet(CUSTOM_WIDGET)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_abovethreshold)
        self.verticalLayout_9.setContentsMargins(12, -1, -1, -1)
        self.verticalLayout_9.setSpacing(0)
        
        self.label_abovethreshold = QtWidgets.QLabel(self.widget_abovethreshold)
        self.label_abovethreshold.setStyleSheet(self.set_label_stylesheet(padding_left=10))
        self.label_abovethreshold.setText('Above threshold')
        self.verticalLayout_9.addWidget(self.label_abovethreshold)
        
        self.label_int_abovethreshold = QtWidgets.QLabel(self.widget_abovethreshold)
        self.label_int_abovethreshold.setStyleSheet(self.set_label_stylesheet(font_size=25, padding_left=10))
        self.label_int_abovethreshold.setText('0')
        self.verticalLayout_9.addWidget(self.label_int_abovethreshold)

        self.widget_max = QtWidgets.QWidget(self.widget_calculatedreadings)
        self.widget_max.setStyleSheet(CUSTOM_WIDGET)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_max)
        self.verticalLayout.setContentsMargins(12, 12, -1, 12)
        self.verticalLayout.setSpacing(0)
        
        self.label_max = QtWidgets.QLabel(self.widget_max)
        self.label_max.setStyleSheet(self.set_label_stylesheet(padding_left=10))
        self.label_max.setText('Maximum')
        self.verticalLayout.addWidget(self.label_max)

        self.label_int_max = QtWidgets.QLabel(self.widget_max)
        self.label_int_max.setStyleSheet(self.set_label_stylesheet(font_size=25, padding_left=10))
        self.label_int_max.setText('0')
        self.verticalLayout.addWidget(self.label_int_max)

        self.gridLayout_2.addWidget(self.widget_mean, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget_numreadings, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_min, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget_stddeviation, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget_abovethreshold, 4, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget_max, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_calculatedreadings, 2, 0, 1, 2)
