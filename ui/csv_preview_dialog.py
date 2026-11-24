from PyQt6 import QtWidgets

CUSTOM_TABLE = (
    "QTableWidget {"
        "background-color: rgb(46, 49, 70);"
        "alternate-background-color: rgb(52, 56, 78);"
        "color: rgb(236, 236, 236);"
        "border: 1px solid rgb(65, 69, 90);"
        "border-radius: 10px;"
        "gridline-color: rgb(65, 69, 90);"
        "selection-background-color: rgb(76, 95, 140);"
        "selection-color: rgb(255, 255, 255);"
        "font-size: 12px;"
        "outline: none;"
    "}"

    "QTableWidget::item {"
        "padding: 6px 10px;"
        "border: none;"
    "}"

    "QTableWidget::item:selected {"
        "background-color: rgb(76, 95, 140);"
        "color: rgb(255, 255, 255);"
    "}"

    "QHeaderView::section {"
        "background-color: rgb(58, 62, 85);"
        "color: rgb(236, 236, 236);"
        "border: none;"
        "border-right: 1px solid rgb(75, 79, 100);"
        "border-bottom: 1px solid rgb(75, 79, 100);"
        "padding: 8px 10px;"
        "font-size: 12px;"
        "font-weight: bold;"
    "}"

    "QTableCornerButton::section {"
        "background-color: rgb(58, 62, 85);"
        "border: none;"
    "}"

    "QScrollBar:vertical {"
        "background: rgb(46, 49, 70);"
        "width: 10px;"
        "margin: 2px;"
        "border: none;"
    "}"

    "QScrollBar::handle:vertical {"
        "background: rgb(112, 112, 112);"
        "border-radius: 5px;"
        "min-height: 25px;"
    "}"

    "QScrollBar::handle:vertical:hover {"
        "background: rgb(135, 135, 145);"
    "}"

    "QScrollBar:horizontal {"
        "background: rgb(46, 49, 70);"
        "height: 10px;"
        "margin: 2px;"
        "border: none;"
    "}"

    "QScrollBar::handle:horizontal {"
        "background: rgb(112, 112, 112);"
        "border-radius: 5px;"
        "min-width: 25px;"
    "}"

    "QScrollBar::handle:horizontal:hover {"
        "background: rgb(135, 135, 145);"
    "}"

    "QScrollBar::add-line, QScrollBar::sub-line {"
        "width: 0px;"
        "height: 0px;"
        "border: none;"
    "}"

    "QScrollBar::add-page, QScrollBar::sub-page {"
        "background: none;"
    "}"
)


class CSVPreviewDialog(QtWidgets.QDialog):
    def __init__(self, dataset, parent=None):
        super().__init__(parent)

        self.setWindowTitle("CSV Preview")
        self.resize(700, 400)

        layout = QtWidgets.QVBoxLayout(self)
        self.table = QtWidgets.QTableWidget()
        self.table.setStyleSheet(CUSTOM_TABLE)

        self.table.setAlternatingRowColors(True)
        self.table.setShowGrid(False)

        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setHighlightSections(False)

        headers = dataset[0] if dataset else []
        preview = dataset[1:]

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

    #@override
    def accept(self):
        if not self.get_selected_columns():
            QtWidgets.QMessageBox.warning(self, "No columns selected", "Please select at least one column." )
            return

        super().accept()