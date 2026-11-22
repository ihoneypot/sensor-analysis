import sys
import csv

import math
import numpy as np

from datetime import datetime
from pathlib import Path

from PyQt6.QtWidgets import QApplication, QDialog
from ui.dataAnalysis import Ui_MainWindow


from ui.csv_preview_dialog import CSVPreviewDialog


class SensorMonitor(Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Callback functions
        self.wdg_datasel_bt_apply.clicked.connect(self.run)
        self.csv_requested.connect(self.open_csv)

        self.csv_file = []
        self.selected_columns = 0
        self.outliers = []
        self.dataset_accepted = False

    def detect_column_types(self, data):
        converted = np.empty(data.shape, dtype=object)
        column_types = []

        for col in range(data.shape[1]):
            values = data[:, col]

            try:
                converted[:, col] = values.astype(int)
                column_types.append("int")
                continue
            except ValueError:
                pass

            try:
                converted[:, col] = values.astype(float)
                column_types.append("float")
                continue
            except ValueError:
                pass

            try:
                converted[:, col] = [
                    datetime.fromisoformat(v) for v in values
                ]
                column_types.append("datetime")
                continue
            except ValueError:
                pass

            converted[:, col] = values
            column_types.append("str")

        return converted, column_types

    def open_csv(self, filename):
        try:
            with open(filename, newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                self.csv_file = list(reader)

        except (OSError, ValueError, csv.Error) as error:
            self.show_error("Cannot load CSV", str(error))
            return

        if not self.csv_file or len(self.csv_file) < 2:
            self.show_error("Cannot load CSV", "CSV contains no data")
            return

        dialog = CSVPreviewDialog(self.csv_file, self)
        

        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.dataset_accepted = True
            self.selected_columns = dialog.get_selected_columns()
            return
    
    def find_outliers(self, numeric_column):
        threshold = float(self.wdg_datasel_lineEdit_alertthreashold.text())
        return numeric_column[numeric_column > threshold]

     
    def calculate_statistics(self):        
        headers = self.csv_file[0]
        selected_names = [headers[i] for i in self.selected_columns]

        data = np.asarray(self.csv_file[1:])
        filtered_dataset = data[:, self.selected_columns]
        converted_data, column_types = self.detect_column_types(filtered_dataset)

        for i, column_type in enumerate(column_types):
            if column_type not in ("int", "float"):
                print("Skipping non-numeric column")
                continue

            numeric_column = converted_data[:, i].astype(float)

            maximum = np.max(numeric_column)
            minimum = np.min(numeric_column)
            mean = np.mean(numeric_column)
            std_deviation = np.std(numeric_column)

            self.label_int_max.setText(str(maximum))
            self.label_int_mean.setText(str(mean))
            self.label_int_min.setText(str(minimum))
            self.label_int_stddeviation.setText(str(std_deviation))
            self.label_int_abovethreshold.setText(str(np.count_nonzero(numeric_column > float(self.wdg_datasel_lineEdit_alertthreashold.text()))))
            self.label_int_numreadings.setText(str(numeric_column.size))

            self.outliers.append(self.find_outliers(numeric_column))
            print(f"Outliers for {selected_names[i]}: {self.outliers[-1]}") 
       

    def run(self):
        if not self.dataset_accepted:
            self.show_error("", "No dataset accepted")
            return

        error = ""
        if self.wdg_datasel_checkBox_randomdata.isChecked():
            if not self.wdg_datasel_lineEdit_numreadings.text():
                error += "For Number of readings\n"

            if not self.wdg_datasel_lineEdit_max.text():
                error += "For Maximum\n"

            if not self.wdg_datasel_lineEdit_min.text():
                error += "For Minimum\n"

        if not self.wdg_datasel_lineEdit_alertthreashold.text():
            error += "For Alert Threshold\n\n"

        if error:
            error += "Please insert a number!"
            self.show_error("", error)
            return

        self.calculate_statistics()



def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Sensor Analysis")
    window = SensorMonitor()
    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
