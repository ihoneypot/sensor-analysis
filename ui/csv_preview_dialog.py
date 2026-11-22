from PyQt6 import QtWidgets

class CSVPreviewDialog(QtWidgets.QDialog):
    def __init__(self, dataset, parent=None):
        super().__init__(parent)

        self.setWindowTitle("CSV Preview")
        self.resize(700, 400)

        layout = QtWidgets.QVBoxLayout(self)

        self.table = QtWidgets.QTableWidget()

        headers = dataset[0] if dataset else []
        preview = dataset[1:11]

        self.table.setColumnCount(len(headers))
        self.table.setRowCount(len(preview) + 1)
        self.table.setHorizontalHeaderLabels(headers)

        for col in range(len(headers)):
            checkbox = QtWidgets.QCheckBox()
            checkbox.setChecked(False)

            container = QtWidgets.QWidget()
            checkbox_layout = QtWidgets.QHBoxLayout(container)
            checkbox_layout.addWidget(checkbox)
            checkbox_layout.setContentsMargins(0, 0, 0, 0)

            self.table.setCellWidget(0, col, container)

        for row_index, row in enumerate(preview, start=1):
            for col_index, value in enumerate(row[:len(headers)]):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.table.setItem(row_index, col_index, item)

        self.table.resizeColumnsToContents()

        self.table.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )

        layout.addWidget(self.table)

        buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.StandardButton.Ok |
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
    
    def get_selected_columns(self):
        selected = []

        for col in range(self.table.columnCount()):
            container = self.table.cellWidget(0, col)
            checkbox = container.findChild(QtWidgets.QCheckBox)

            if checkbox.isChecked():
                selected.append(col)

        return selected

    # @override accept of super class 
    def accept(self):
        if not self.get_selected_columns():
            QtWidgets.QMessageBox.warning(self, "No columns selected", "Please select at least one column." )
            return

        super().accept()