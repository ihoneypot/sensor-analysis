import sys
import csv

import math
import numpy as np

from datetime import datetime
from pathlib import Path

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox

from ui.dataAnalysis import Ui_MainWindow
from ui.csv_preview_dialog import CSVPreviewDialog


class SensorMonitor(Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = FigureCanvas(Figure(figsize=(8, 5)))
        self.widget_plot.layout().addWidget(self.canvas)
        self.canvas.hide()

        self.histogram_canvas = FigureCanvas(Figure(figsize=(8, 5)))
        self.widget_histogram.layout().addWidget(self.histogram_canvas)
        self.histogram_canvas.hide()

        # Callback functions
        self.wdg_datasel_lineEdit_filepath.returnPressed.connect(lambda: self.on_open_csv(self.wdg_datasel_lineEdit_filepath.text()))
        self.wdg_datasel_bt_OpenFile.clicked.connect(self.on_open_file)
        self.wdg_datasel_bt_apply.clicked.connect(self.run)
        self.wdg_datasel_bt_save.clicked.connect(self.on_save)
        self.wdg_datasel_bt_clear.clicked.connect(self.on_clear)

        self.csv_file = []
        self.dataset = []
        self.plot_image = []
        self.histogram_image = []
        self.selected_columns = 0
        self.dataset_accepted = False

    def save_csv(self, path, filename, dataset):
        try:

            filepath = Path(path) / f"{filename}.csv"

            with filepath.open("w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(dataset["headers"])
                writer.writerows(dataset["data"])

            return True

        except (OSError, csv.Error, ValueError, TypeError, KeyError) as error:
            self.show_error("Cannot write CSV", f"{filename}.csv: {error}")
            return False
    
    def on_save(self):
        if not self.csv_file and not self.dataset:
            self.show_error("Nothing to save", "Upload a file or generate readings first" )
            return

        timestamp = datetime.now().strftime("%d%m%Y%H%M%S")
        path = QFileDialog.getExistingDirectory(self, "Select save directory", "")
        if not path:
            return

        path = Path(path)

        key = next((k for k in self.dataset if k.startswith("calculated_stats_")), None)

        if key is not None:
            self.save_csv(path=path, filename=f"{key}_{timestamp}", dataset=self.dataset[key])

        
        if "headers" in self.dataset and "data" in self.dataset:
            sensor_type = next(
                (header for header, dtype in zip(self.dataset["headers"], self.dataset["types"])
                if dtype in ("int", "float")),
                "sensor_data"
            ).replace(" ", "")

            self.save_csv(path=path, filename=f"{sensor_type}_{timestamp}", dataset=self.dataset)


        for name, images in (
            ("plot", self.plot_image),
            ("histogram", self.histogram_image)
        ):
            for index, image in enumerate(images, start=1):
                if image is None:
                    continue

                filename = f"{name}_{timestamp}.png"

                try:
                    filepath = path / filename

                    if not image.save(str(filepath)):
                        raise OSError("Image could not be saved")

                except (OSError, RuntimeError, TypeError) as error:
                    self.show_error("Cannot save image", f"{filename}: {error}")
        
        QMessageBox.information(
            self,
            "Save completed",
            f"Data successfully saved to:\n{path}"
        )

    def on_clear(self):
        self.label_plot.show()
        self.label_showhistogram.show()
        
        self.wdg_datasel_lineEdit_filepath.setText("")
        self.wdg_datasel_lineEdit_numreadings.setText("")
        self.wdg_datasel_lineEdit_max.setText("")
        self.wdg_datasel_lineEdit_min.setText("")
        self.wdg_datasel_lineEdit_alertthreashold.setText("")
        self.label_int_mean.setText("0")
        self.label_int_max.setText("0")
        self.label_int_min.setText("0")
        self.label_int_abovethreshold.setText("0")
        self.label_int_stddeviation.setText("0")
        self.label_int_numreadings.setText("0")

        self.canvas.hide()
        self.histogram_canvas.hide()

        self.dataset_accepted = False  
        self.dataset = []
        self.csv_file = []

    def on_open_csv(self, filename):
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
    
    def on_open_file(self):
        path, _ = QFileDialog.getOpenFileName(None, 'Open sensor readings', "", "CSV files (*.csv);;All files (*)")
        self.wdg_datasel_lineEdit_filepath.setText(path)
        if not path:
            self.show_error("Pathnot found", "try again or solve manually")
            return
        
        self.on_open_csv(path)

    def generate_readings(self):
        num_read = int(self.wdg_datasel_lineEdit_numreadings.text())
        min_val = float(self.wdg_datasel_lineEdit_min.text())
        max_val = float(self.wdg_datasel_lineEdit_max.text())
        sensor = self.wdg_datasel_comboBox_sensortype.currentText().replace(" ","")

        if sensor == "Tempsensor":
            if num_read < 3 or min_val >= max_val:
                raise ValueError("Invalid number of readings or min/max range")

            data = self.sensor_readings(num_read, min_val, max_val, noise=0.03)
            
        elif sensor == "Humiditysensor":
            if num_read < 3 or not (0 <= min_val < max_val <= 100):
                raise ValueError("Humidity must be between 0 and 100%, with at least 3 readings")

            data = self.sensor_readings(num_read, min_val, max_val, noise=0.2)

        else:
            raise ValueError("Sensor not supported yet")

        return {
            "headers": [
                sensor,
                "last_changed"
            ],
            "types": ["float", "datetime"],
            "data": data
        }   

    def sensor_readings(self, num_read, min_val, max_val, noise=0.03):
        rng = np.random.default_rng()
        start_time = np.datetime64(datetime.now(), "s")

        num_checkpoints = min(num_read, max(3, num_read // 100 + 2))

        checkpoints = rng.uniform(min_val, max_val, num_checkpoints)
        checkpoints[0] = min_val
        checkpoints[num_checkpoints // 2] = max_val

        checkpoint_positions = np.linspace(
            0, num_read - 1, num_checkpoints
        )

        values = np.interp(
            np.arange(num_read),
            checkpoint_positions,
            checkpoints
        )

        values += rng.normal(0, noise, num_read)
        values = np.clip(values, min_val, max_val)

        values[0] = min_val
        values[int(round(checkpoint_positions[num_checkpoints // 2]))] = max_val

        timestamps = (
            start_time + np.arange(num_read) * np.timedelta64(1, "s")
        )

        data = np.empty((num_read, 2), dtype=object)
        data[:, 0] = values
        data[:, 1] = timestamps

        return data
  
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

    def find_outliers(self, numeric_column):
        threshold = float(self.wdg_datasel_lineEdit_alertthreashold.text())
        return numeric_column[numeric_column > threshold]

    def stats_from_file(self):
        headers = self.csv_file[0]
        selected_names = [headers[i] for i in self.selected_columns]
        num_read = self.wdg_datasel_lineEdit_numreadings.text()

        data = np.asarray(
            self.csv_file[1:int(num_read) + 1] if num_read else self.csv_file[1:]
        )

        filtered_data = data[:, self.selected_columns]
        converted_data, column_types = self.detect_column_types(filtered_data)

        return {
            "headers": selected_names,
            "types": column_types,
            "data": converted_data
        }

    def calculate_statistics(self, dataset):
        data = dataset["data"]
        headers = dataset["headers"]
        types = dataset["types"]

        threshold = float(self.wdg_datasel_lineEdit_alertthreashold.text())

        datetime_index = next((i for i, dtype in enumerate(types) if dtype == "datetime"), None)

        timestamps = (
            data[:, datetime_index]
            if datetime_index is not None else None
        )

        for i, dtype in enumerate(types):
            if dtype not in ("int", "float"):
                continue

            values = data[:, i].astype(float)

            if values.size == 0:
                continue

            maximum = np.max(values)
            minimum = np.min(values)
            mean = np.mean(values)
            std_deviation = np.std(values)
            outliers = self.find_outliers(values)
            above_thresh = np.count_nonzero(values > threshold)
            num_readings = values.size
            saved_time = np.datetime64(datetime.now().isoformat(timespec="seconds"))
            
            dataset[f"calculated_stats_{headers[i].replace(" ", "")}"] = {
                "headers": ["datetime", "min_val", "max_val", "mean_val", "number_readings", "std_dev", "above_threshold"],
                "data": [[saved_time, minimum, maximum, mean, num_readings, std_deviation, above_thresh]]
            }

            self.label_int_max.setText(f"{maximum:.2f}")
            self.label_int_min.setText(f"{minimum:.2f}")
            self.label_int_mean.setText(f"{mean:.2f}")
            self.label_int_stddeviation.setText(f"{std_deviation:.2f}")
            self.label_int_abovethreshold.setText(str(above_thresh))
            self.label_int_numreadings.setText(str(num_readings))

            try:
                self.plot_readings(
                    values=values,
                    threshold=threshold,
                    outliers=outliers,
                    timestamps=timestamps,
                    title=headers[i]
                )

                self.plot_histogram(
                    values=values,
                    threshold=threshold,
                    title=headers[i]
                )

            except (ValueError, TypeError, IndexError, RuntimeError, AttributeError) as error:
                self.show_error("Plotting error", str(error))

    def plot_readings(self, values, threshold, outliers, timestamps=None, title="Sensor readings"):
        self.canvas.figure.clear()

        ax = self.canvas.figure.add_subplot(111)
        x = timestamps if timestamps is not None else np.arange(len(values))
        ax.plot(x, values, color="blue", label="Sensor reading")

        ax.axhline(
            y=threshold,
            color="red",
            linestyle="--",
            label=f"Alert threshold: {threshold:g}"
        )

        # readings above threshold
        mask = np.isin(values, outliers)
        
        ax.scatter(
            x[mask],
            values[mask],
            color="red",
            s=20,
            label="Above threshold",
            zorder=3
        )

        ax.set_title(f"Recorded readings - {title}")
        ax.set_xlabel("Time" if timestamps is not None else "Sample number")    
        ax.set_ylabel("Sensor reading")
        ax.grid(True, alpha=0.3)
        ax.legend(loc="upper right")

        self.canvas.figure.tight_layout()
        self.canvas.draw()
        self.canvas.show()
        self.plot_image.append(self.canvas.grab())
    
    def plot_histogram(self, values, threshold, title="Sensor readings"):
        
        self.histogram_canvas.figure.clear()
        ax = self.histogram_canvas.figure.add_subplot(111)

        ax.hist(
            values,
            bins=10,
            color="#4285F4",
            edgecolor="white"
        )

        ax.axvline(
            x=threshold,
            color="red",
            linestyle="--",
            label=f"Alert threshold: {threshold:g}"
        )

        ax.set_title(f"Reading distribution\n{title}")
        ax.set_xlabel("Sensor reading")
        ax.set_ylabel("Number of readings")

        ax.grid(True, alpha=0.3)
        ax.set_axisbelow(True)
        ax.legend(loc="upper right")

        self.histogram_canvas.figure.tight_layout()
        self.histogram_canvas.draw()
        self.histogram_canvas.show()
        self.histogram_image.append(self.histogram_canvas.grab())


    def run(self):
        self.label_plot.hide()
        self.label_showhistogram.hide()

        if not self.wdg_datasel_checkBox_randomdata.isChecked() and not self.dataset_accepted:
            self.show_error("No dataset accepted", "Please select a csv file to start the analysis")
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
            self.show_error("Start Analysis", str(error))
            return

        try:
            if self.wdg_datasel_checkBox_randomdata.isChecked():
                self.dataset = self.generate_readings()
            else:
                self.dataset = self.stats_from_file()

            self.calculate_statistics(self.dataset)

        except (ValueError, TypeError, IndexError, RuntimeError, AttributeError) as error:
            self.show_error("Dataset error:", str(error))

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Sensor Analysis")
    window = SensorMonitor()
    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
