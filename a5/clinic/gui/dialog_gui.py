import sys
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QPlainTextEdit
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QStackedLayout
from PyQt6.QtWidgets import QTableView, QPlainTextEdit, QFormLayout
from PyQt6.QtWidgets import QDateEdit, QDialog, QDialogButtonBox, QInputDialog
from clinic.controller import Controller
from clinic.gui.login_window_gui import LoginWindow
from clinic.gui.patient_table_model import PatientTableModel
from clinic.gui.patient_table_gui import PatientTableGUI

# shows when updating patient, asks for the old phn and confirms if the update can proceed
class Update_Dialogue(QDialog):
    def __init__(self, controller, main_window):
        super().__init__()

        self.controller = controller
        self.main_window = main_window
        self.setWindowTitle("Confirm phn")
        self.message = QMessageBox(self)

        layout = QGridLayout()
        self.label = QLabel("Please confirm the original phn of the patient you wish to update")
        self.line = QLineEdit()

        QBtn = (QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.update_confirmed)
        self.buttonBox.rejected.connect(self.reject)

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.line, 1, 0)
        layout.addWidget(self.buttonBox, 2, 0)

        self.setLayout(layout)

    def update_confirmed(self):
        try:
            phn = self.line.text()
            phn = int(phn)
            patient = self.controller.search_patient(phn)
            if patient:
                self.main_window.original_phn = phn
                self.accept()
            else:
                self.message.warning(self, "Fail", "Could not update patient")
                self.reject()
        except:
            self.message.warning(self, "Fail", "Could not update patient")
            self.reject()

# shown when deleting a patient, asks if user is sure they want to then deletes
class Delete_Dialogue(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Confirm Deletion")

        QBtn = (QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Are you sure you want to delete this patient?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class Update_Note_Dialogue(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Update the note now")

        QBtn = (QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Please select OK then update the contents of the note as desired then press Update Note again")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
class Delete_Note_Dialogue(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Confirm Deletion")

        QBtn = (QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Are you sure you want to delete this note?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)