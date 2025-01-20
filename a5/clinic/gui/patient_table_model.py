import sys
from PyQt6.QtCore import Qt, QAbstractTableModel

from clinic.controller import Controller
from clinic.patient import Patient


class PatientTableModel(QAbstractTableModel):
    def __init__(self, controller, patient_list):
        super().__init__()
        self.controller = controller
        self._data = []
        self.patient_list = patient_list
        self.refresh_data(self.patient_list)

    def refresh_data(self, patient_list):
        self._data = []
        self.patient_list = patient_list

        if self.controller.is_logged:
            #patients = self.controller.list_patients()
            for patient in self.patient_list:
                self._data.append([patient.phn, patient.name, patient.birth_date, patient.phone, patient.email, patient.address])
            # emitting the layoutChanged signal to alert the QTableView of model changes
            self.layoutChanged.emit()

    def reset(self):
        self._data = []
        # emitting the layoutChanged signal to alert the QTableView of model changes
        self.layoutChanged.emit()

    def data(self, index, role):
        value = self._data[index.row()][index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            # Perform per-type checks and render accordingly.
            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value
            if isinstance(value, str):
                # Render strings with quotes
                return '%s' % value
            # Default (anything not captured above: e.g. int)
            return value

        if role == Qt.ItemDataRole.TextAlignmentRole:
            if isinstance(value, int) or isinstance(value, float):
                # Align right, vertical middle.
                return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignRight

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        if self._data:
            return len(self._data[0])
        else:
            return 0

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        headers = ['phn', 'Name', 'Birth Date', 'Phone', 'Email', 'Address']
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return '%s' % headers[section]
        return super().headerData(section, orientation, role)
