import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt6.QtWidgets import QPushButton, QTableView, QWidget

from clinic.controller import Controller
from clinic.patient import Patient
from clinic.gui.patient_table_model import PatientTableModel
from clinic.gui.list_patient_gui import ListPatientGUI

class PatientTableGUI(QMainWindow):

    def __init__(self, controller, patient_list, search):
        super().__init__()
        self.controller = controller
        self.patient_list = patient_list
        self.search = search
        self.setWindowTitle("Patients")
        self.resize(750, 400)

        # add sub windows
        self.list_patient_gui = ListPatientGUI(self.controller)

        self.patient_table = QTableView()

        self.patient_model = PatientTableModel(self.controller, self.patient_list)
        self.patient_table.setModel(self.patient_model)

        # connect the double click signal to allow storing the current product's code
        self.current_patient_phn = None
        self.patient_table.doubleClicked.connect(self.list_patient_requested)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.setMaximumWidth(250)

        self.refresh_button.clicked.connect(self.refresh_table)

        layout = QVBoxLayout()
        layout.addWidget(self.patient_table)
        layout.addWidget(self.refresh_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.refresh_table()

    def refresh_table(self):
        self.patient_list = self.controller.retrieve_patients(self.search)
        self.patient_model.refresh_data(self.patient_list)
        self.patient_table.setEnabled(False)
        self.patient_table.setColumnWidth(1, 200)

    def list_patient_requested(self):
        index = self.patient_table.selectionModel().currentIndex()
        self.current_patient_code = int(index.sibling(index.row(), 0).data())
        
        self.list_patient_gui.list_patient(self.current_patient_phn)
        self.list_patient_gui.show()