import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

from clinic.controller import Controller

class ListPatientGUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("List Patient")

        layout1 = QGridLayout()

        label_phn = QLabel("Patient phn")
        self.text_phn = QLineEdit()
        self.text_phn.setInputMask('00000000')
        label_name = QLabel("Name")
        self.text_name = QLineEdit()
        label_birthdate = QLabel("Birth Date")
        self.text_birthdate = QLineEdit()
        label_phone = QLabel("Phone")
        self.text_phone = QLineEdit()
        label_email = QLabel("Email")
        self.text_email = QLineEdit()
        label_address = QLabel("Address")
        self.text_address = QLineEdit()

        layout1.addWidget(label_phn, 0, 0)
        layout1.addWidget(self.text_phn, 0, 1)
        layout1.addWidget(label_name, 1, 0)
        layout1.addWidget(self.text_name, 1, 1)
        layout1.addWidget(label_birthdate, 2, 0)
        layout1.addWidget(self.text_birthdate, 2, 1)
        layout1.addWidget(label_phone, 3, 0)
        layout1.addWidget(self.text_phone, 3, 1)
        layout1.addWidget(label_email, 4, 0)
        layout1.addWidget(self.text_email, 4, 1)
        layout1.addWidget(label_address, 5, 0)
        layout1.addWidget(self.text_address, 5, 1)

        layout2 = QHBoxLayout()

        self.button_update = QPushButton("Update")
        self.button_delete = QPushButton("Delete")
        self.button_close = QPushButton("Close")
        layout2.addWidget(self.button_update)
        layout2.addWidget(self.button_delete)
        layout2.addWidget(self.button_close)

        layout3 = QVBoxLayout()

        top_widget = QWidget()
        top_widget.setLayout(layout1)
        bottom_widget = QWidget()
        bottom_widget.setLayout(layout2)
        layout3.addWidget(top_widget)
        layout3.addWidget(bottom_widget)
        widget = QWidget()
        widget.setLayout(layout3)

        self.setCentralWidget(widget)

        # define widgets' initial state
        self.text_phn.setEnabled(False)
        self.text_name.setEnabled(False)
        self.text_birthdate.setEnabled(False)
        self.text_phone.setEnabled(False)
        self.text_email.setEnabled(False)
        self.text_address.setEnabled(False)
        self.button_close.setEnabled(True)

        # connect the button's clicked signal to the slot below
        self.button_close.clicked.connect(self.close_button_clicked)


    def list_patient(self, key):
        ''' search and list product '''
        patient = self.controller.search_patient(key)
        message = QMessageBox
        if patient:
            self.text_phn.setText(str(patient.phn))
            self.text_name.setText(patient.name)
            self.text_birthdate.setText(patient.birthdate)
            self.text_phone.setText(patient.phone)
            self.text_email.setText(patient.email)
            self.text_address.setText(patient.address)
        else:
            message.warning(self, "fail", "no product was found")
            
        self.text_phn.setEnabled(False)
        self.text_name.setEnabled(False)
        self.text_birthdate.setEnabled(False)
        self.text_phone.setEnabled(False)
        self.text_address.setEnabled(False)
        self.button_close.setEnabled(True)

    def close_button_clicked(self):
        ''' 'close list product window '''
        self.hide()


    def closeEvent(self, event):
        self.close_button_clicked()