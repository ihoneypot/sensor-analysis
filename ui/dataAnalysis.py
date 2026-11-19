from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
ICO_FOLDER = f'{ROOT_PATH}/imgs/folder3.ico'
DOWNROW = f'{ROOT_PATH}/imgs/downrow.png'

custom_widget_style = ( 
    "QWidget{"
        "border-radius: 10px;"
        " background-color: rgb(46, 49, 70);"
    "}"
)

BODY_LINEEDIT = (
    "QLineEdit {\n"
    "    background-color: rgb(112, 112, 112);\n"
    "    color: rgb(236, 236, 236);\n"
    "    border: none;\n"
    "    border-radius: 10px;\n"
    "    padding: 0px 4px;\n"
    "    height: 30px;\n"
    "}\n"
    "QLineEdit:focus {\n"
    "    border-radius: 10px;\n"
    "}\n"
)

COMBOBOX2 = (
    "QComboBox {"
    "    background-color: rgb(112, 112, 112);"
    "    color: rgb(236, 236, 236);"
    "    border: none;"
    "    border-radius: 10px;"
    "    height: 30px;"
    "}"
    "QComboBox::drop-down {"
        "border-radius: 10px;"
    "}"
    "QComboBox::down-arrow {"
        f"image: url({DOWNROW});"
        "width: 12px;"
        "height: 12px;"
        "margin-right: 15px;"
    "}"
)

BODY_LABEL = (
    "background-color: rgba(255, 255, 255, 0);"
    "color: rgb(236, 236, 236);"
)

PBUTTON = (
    "QPushButton{\n"
        f"qproperty-icon: url({ICO_FOLDER});"
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

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.resize(967, 738)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("background-color: rgb(36, 36, 39);")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        self.widget_main = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_main)

        self.widget_dataselection = QtWidgets.QWidget(self.widget_main)
        self.widget_dataselection.setStyleSheet(custom_widget_style)
        # self.widget_dataselection.setMinimumSize(QtCore.QSize(250, 300))
        # self.widget_dataselection.setMaximumSize(QtCore.QSize(300, 350))
        # self.widget_dataselection.setMinimumSize(QtCore.QSize(400, 170))

        self.gridLayout = QtWidgets.QGridLayout(self.widget_dataselection)
        self.gridLayout.setContentsMargins(8, -1, -1, -1)
        
        self.wdg_datasel_lineEdit_filepath = QtWidgets.QLineEdit(self.widget_dataselection)
        self.wdg_datasel_lineEdit_filepath.setStyleSheet(BODY_LINEEDIT)
        self.gridLayout.addWidget(self.wdg_datasel_lineEdit_filepath, 2, 1, 1, 2)

        self.wdg_datasel_comboBox_sensortype = QtWidgets.QComboBox(self.widget_dataselection)
        self.wdg_datasel_comboBox_sensortype.setStyleSheet(COMBOBOX2)
        self.wdg_datasel_comboBox_sensortype.addItem("Temp sensor")
        self.wdg_datasel_comboBox_sensortype.addItem("Pressure sensor")
        self.wdg_datasel_comboBox_sensortype.addItem("Energy sensor")
        self.gridLayout.addWidget(self.wdg_datasel_comboBox_sensortype, 4, 0, 1, 3)

        self.wdg_datasel_label_min = QtWidgets.QLabel(self.widget_dataselection)
        self.wdg_datasel_label_min.setText("Minimum")
        self.gridLayout.addWidget(self.wdg_datasel_label_min, 7, 0, 1, 1)
        
        self.wdg_datasel_label_alertthreshold = QtWidgets.QLabel(self.widget_dataselection)
        self.wdg_datasel_label_alertthreshold.setText("Alert Threshold")
        self.wdg_datasel_label_alertthreshold.setStyleSheet(BODY_LINEEDIT)
        self.gridLayout.addWidget(self.wdg_datasel_label_alertthreshold, 8, 0, 1, 2)
        
        self.wdg_datasel_label_max = QtWidgets.QLabel(self.widget_dataselection)
        self.wdg_datasel_label_max.setStyleSheet(BODY_LINEEDIT)
        self.wdg_datasel_label_max.setText("Maximum")
        self.gridLayout.addWidget(self.wdg_datasel_label_max, 6, 0, 1, 1)

        self.wdg_datasel_lineEdit_alertthreashold = QtWidgets.QLineEdit(self.widget_dataselection)
        self.wdg_datasel_lineEdit_alertthreashold.setStyleSheet(BODY_LINEEDIT)
        self.wdg_datasel_lineEdit_alertthreashold.setMaximumSize(QtCore.QSize(50, 16777215))
        self.wdg_datasel_lineEdit_alertthreashold.setText("")
        self.gridLayout.addWidget(self.wdg_datasel_lineEdit_alertthreashold, 8, 2, 1, 1)

        self.wdg_datasel_bt_OpenFile = QtWidgets.QPushButton(self.widget_dataselection)
        self.wdg_datasel_bt_OpenFile.setText("Open")
        self.wdg_datasel_bt_OpenFile.setStyleSheet(PBUTTON)

        self.gridLayout.addWidget(self.wdg_datasel_bt_OpenFile, 2, 0, 1, 1)

        self.wdg_datasel_label_sensortype = QtWidgets.QLabel(self.widget_dataselection)
        self.wdg_datasel_label_sensortype.setText("Select sesnor type") 
        self.gridLayout.addWidget(self.wdg_datasel_label_sensortype, 3, 0, 1, 3)

        self.wdg_datasel_lineEdit_max = QtWidgets.QLineEdit(self.widget_dataselection)
        self.wdg_datasel_lineEdit_max.setStyleSheet(BODY_LINEEDIT) 
        self.wdg_datasel_lineEdit_max.setMaximumSize(QtCore.QSize(50, 16777215))

        self.gridLayout.addWidget(self.wdg_datasel_lineEdit_max, 6, 2, 1, 1)
        self.wdg_datasel_lineEdit_min = QtWidgets.QLineEdit(self.widget_dataselection)
        self.wdg_datasel_lineEdit_min.setStyleSheet(BODY_LINEEDIT) 
        self.wdg_datasel_lineEdit_min.setMaximumSize(QtCore.QSize(50, 16777215))
        self.wdg_datasel_lineEdit_min.setText("")
        self.gridLayout.addWidget(self.wdg_datasel_lineEdit_min, 7, 2, 1, 1)
        
        self.wdg_datasel_checkBox_randomdata = QtWidgets.QCheckBox(self.widget_dataselection)
        self.wdg_datasel_checkBox_randomdata.setText("Random data")
        self.gridLayout.addWidget(self.wdg_datasel_checkBox_randomdata, 0, 0, 1, 3)

        self.wdg_datasel_label_numberofreadings = QtWidgets.QLabel(self.widget_dataselection)
        self.wdg_datasel_label_numberofreadings.setText("Number of readings ")
        self.wdg_datasel_label_numberofreadings.setStyleSheet(BODY_LABEL)

        self.gridLayout.addWidget(self.wdg_datasel_label_numberofreadings, 5, 0, 1, 2)
        self.wdg_datasel_label_selectsensor = QtWidgets.QLabel(self.widget_dataselection)
        self.wdg_datasel_label_selectsensor.setText("Select sensor file")
        self.gridLayout.addWidget(self.wdg_datasel_label_selectsensor, 1, 0, 1, 3)
        
        self.wdg_datasel_lineEdit_numreadings = QtWidgets.QLineEdit(self.widget_dataselection)
        self.wdg_datasel_lineEdit_numreadings.setStyleSheet(BODY_LINEEDIT) 
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wdg_datasel_lineEdit_numreadings.sizePolicy().hasHeightForWidth())
       
        self.wdg_datasel_lineEdit_numreadings.setSizePolicy(sizePolicy)
        self.wdg_datasel_lineEdit_numreadings.setMaximumSize(QtCore.QSize(50, 16777215))

        self.gridLayout.addWidget(self.wdg_datasel_lineEdit_numreadings, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_dataselection, 0, 0, 2, 1)

        #############################################################
        self.widget_calculatedreadings = QtWidgets.QWidget(self.widget_main)
        self.widget_calculatedreadings.setStyleSheet(custom_widget_style)
        # self.widget_calculatedreadings.setMinimumSize(QtCore.QSize(250, 300))
        # self.widget_calculatedreadings.setMaximumSize(QtCore.QSize(300, 350))

        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_calculatedreadings)

        self.widget_stddeviation = QtWidgets.QWidget(self.widget_calculatedreadings)
        self.widget_stddeviation.setMinimumSize(QtCore.QSize(150, 50))
        self.widget_stddeviation.setMaximumSize(QtCore.QSize(200, 200))





        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_stddeviation)

        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout_8.addLayout(top_layout)



        self.label_stddeviation = QtWidgets.QLabel(self.widget_stddeviation)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_stddeviation.setFont(font)
        self.label_stddeviation.setText("Standard deviation")
        self.verticalLayout_8.addWidget(self.label_stddeviation)

        self.label_int_stddeviation = QtWidgets.QLabel(self.widget_stddeviation)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_int_stddeviation.setFont(font)
        self.label_int_stddeviation.setText("403")
        self.verticalLayout_8.addWidget(self.label_int_stddeviation)

        self.gridLayout_2.addWidget(self.widget_stddeviation, 1, 1, 1, 1)
        self.widget_numreadings = QtWidgets.QWidget(self.widget_calculatedreadings)
        self.widget_numreadings.setMinimumSize(QtCore.QSize(150, 50))
        self.widget_numreadings.setMaximumSize(QtCore.QSize(200, 200))

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_numreadings)

        self.label_readings = QtWidgets.QLabel(self.widget_numreadings)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_readings.setFont(font)
        self.label_readings.setText("Readings")
        self.verticalLayout_5.addWidget(self.label_readings)
        self.label_int_numreadings = QtWidgets.QLabel(self.widget_numreadings)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_int_numreadings.setFont(font)
        self.label_int_numreadings.setText("403")
        self.verticalLayout_5.addWidget(self.label_int_numreadings)
        self.gridLayout_2.addWidget(self.widget_numreadings, 1, 0, 1, 1)
        self.widget_max = QtWidgets.QWidget(self.widget_calculatedreadings)
        self.widget_max.setMinimumSize(QtCore.QSize(150, 50))
        self.widget_max.setMaximumSize(QtCore.QSize(200, 200))

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_max)

        self.label_max = QtWidgets.QLabel(self.widget_max)
        self.label_max.setText("Maximum")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_max.setFont(font)
        
        self.verticalLayout_4.addWidget(self.label_max)
        self.label_int_max = QtWidgets.QLabel(self.widget_max)
        self.label_int_max.setText("403")
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_int_max.setFont(font)

        self.verticalLayout_4.addWidget(self.label_int_max)
        self.gridLayout_2.addWidget(self.widget_max, 0, 0, 1, 1)

        self.widget_mean = QtWidgets.QWidget(self.widget_calculatedreadings)
        self.widget_mean.setMinimumSize(QtCore.QSize(150, 50))
        self.widget_mean.setMaximumSize(QtCore.QSize(200, 200))

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_mean)
        self.label_mean = QtWidgets.QLabel(self.widget_mean)
        self.label_mean.setText("Mean")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_mean.setFont(font)

        self.verticalLayout_6.addWidget(self.label_mean)
        self.label_int_mean = QtWidgets.QLabel(self.widget_mean)
        self.label_int_mean.setText("403")
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_int_mean.setFont(font)

        self.verticalLayout_6.addWidget(self.label_int_mean)
        self.gridLayout_2.addWidget(self.widget_mean, 0, 1, 1, 1)
        self.widget_min = QtWidgets.QWidget(self.widget_calculatedreadings)
        self.widget_min.setMinimumSize(QtCore.QSize(150, 50))
        self.widget_min.setMaximumSize(QtCore.QSize(200, 200))

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_min)

        self.label_min = QtWidgets.QLabel(self.widget_min)
        self.label_min.setText("Minimum")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_min.setFont(font)

        self.verticalLayout_7.addWidget(self.label_min)
        self.label_int_min = QtWidgets.QLabel(self.widget_min)
        self.label_int_min.setText("403")
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_int_min.setFont(font)

        self.verticalLayout_7.addWidget(self.label_int_min)
        self.gridLayout_2.addWidget(self.widget_min, 0, 2, 1, 1)
        self.widget_abovethreshold = QtWidgets.QWidget(self.widget_calculatedreadings)
        self.widget_abovethreshold.setMinimumSize(QtCore.QSize(150, 50))
        self.widget_abovethreshold.setMaximumSize(QtCore.QSize(200, 200))

        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_abovethreshold)

        self.label_abovethreshold = QtWidgets.QLabel(self.widget_abovethreshold)
        self.label_abovethreshold.setText("Above threshold")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_abovethreshold.setFont(font)

        self.verticalLayout_9.addWidget(self.label_abovethreshold)
        self.label_int_abovethreshold = QtWidgets.QLabel(self.widget_abovethreshold)
        self.label_int_abovethreshold.setText("403")
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_int_abovethreshold.setFont(font)

        self.verticalLayout_9.addWidget(self.label_int_abovethreshold)
        self.gridLayout_2.addWidget(self.widget_abovethreshold, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.widget_calculatedreadings, 0, 1, 1, 1)
        
        #############################################################
        self.widget_histogram = QtWidgets.QWidget(self.widget_main)
        self.widget_histogram.setStyleSheet(custom_widget_style)
        self.widget_histogram.setMinimumSize(QtCore.QSize(250, 250))

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_histogram)

        self.label_showplot = QtWidgets.QLabel(self.widget_histogram)
        self.label_showplot.setText("Show the plot here")
        self.verticalLayout_3.addWidget(self.label_showplot)
        self.gridLayout_3.addWidget(self.widget_histogram, 1, 1, 2, 1)
        self.widget_plot = QtWidgets.QWidget(self.widget_main)
        self.widget_plot.setStyleSheet(custom_widget_style)
        self.widget_plot.setMinimumSize(QtCore.QSize(250, 250))

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_plot)

        self.label_showhistogram = QtWidgets.QLabel(self.widget_plot)
        self.label_showhistogram.setText("Show histogram here ")
        self.verticalLayout_2.addWidget(self.label_showhistogram)
        self.gridLayout_3.addWidget(self.widget_plot, 2, 0, 1, 1)
        
        self.verticalLayout.addWidget(self.widget_main)
        self.setCentralWidget(self.centralwidget)