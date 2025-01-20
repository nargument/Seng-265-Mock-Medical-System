import sys
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QPlainTextEdit
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QStackedLayout
from PyQt6.QtWidgets import QTableView, QPlainTextEdit, QFormLayout, QAbstractScrollArea
from PyQt6.QtWidgets import QDateEdit, QDialog, QDialogButtonBox, QInputDialog
from clinic.controller import Controller
from clinic.gui.login_window_gui import LoginWindow
from clinic.gui.patient_table_model import PatientTableModel
from clinic.gui.patient_table_gui import PatientTableGUI
from clinic.gui.dialog_gui import *
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.exception.duplicate_login_exception import DuplicateLoginException
from clinic.exception.invalid_logout_exception import InvalidLogoutException
from clinic.exception.illegal_access_exception import IllegalAccessException
from clinic.exception.illegal_operation_exception import IllegalOperationException
from clinic.exception.no_current_patient_exception import NoCurrentPatientException

class ClinicGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.controller = Controller(True)      
        self.setWindowTitle("Clinic")
        self.login_window = LoginWindow(self.controller, self)

        self.login_window.show()

        # define the multiple layouts used to create the layout for the main window
        self.main_layout = QGridLayout()
        layout1 = QGridLayout()             # patient operation buttons
        layout2 = QGridLayout()             # Current patient display
        layout3 = QHBoxLayout()             # Current patient buttons
        layout4 = QGridLayout()             # logout and quit buttons

        # make all the buttons and the label for layout 1
        label_welcome = QLabel("Select an option:")
        self.button_create_patient = QPushButton("Create Patient")
        self.button_search_patient = QPushButton("Search Patient")
        self.button_retrieve_patients = QPushButton("Retrieve Patients")
        self.button_update_patient = QPushButton("Update Patient")
        self.button_delete_patient = QPushButton("Delete Patient")
        self.button_list_patients = QPushButton("List Patients")
        self.button_begin_appointment = QPushButton("Begin Appointment")
        self.button_clear = QPushButton("Clear")

        # set the max width of all the layout 1 buttons to 125
        self.button_create_patient.setMaximumWidth(125)
        self.button_search_patient.setMaximumWidth(125)
        self.button_retrieve_patients.setMaximumWidth(125)
        self.button_update_patient.setMaximumWidth(125)
        self.button_delete_patient.setMaximumWidth(125)
        self.button_list_patients.setMaximumWidth(125)
        self.button_begin_appointment.setMaximumWidth(125)
        self.button_clear.setMaximumWidth(125)

        # add all the layout 1 widgets to layout 1
        layout1.addWidget(label_welcome, 0, 0)
        layout1.addWidget(self.button_create_patient, 1, 0)
        layout1.addWidget(self.button_search_patient, 2, 0)
        layout1.addWidget(self.button_retrieve_patients, 3, 0)
        layout1.addWidget(self.button_update_patient, 4, 0)
        layout1.addWidget(self.button_delete_patient, 5, 0)
        layout1.addWidget(self.button_list_patients, 6, 0)
        layout1.addWidget(self.button_begin_appointment, 7, 0)
        layout1.addWidget(self.button_clear, 8, 0)

        layout1.setVerticalSpacing(2)

        # add layout1 to the main
        self.main_layout.addLayout(layout1, 0, 0)

        #make all the labels and buttuns for layout2
        self.label_cur_patient = QLabel("Current Patient")
        self.label_phn = QLabel("PHN:")
        self.label_name = QLabel("Name:")
        self.label_birth_date = QLabel("Birth Date:")
        self.label_phone = QLabel("Phone Number:")
        self.label_email = QLabel("Email:")
        self.label_address = QLabel("Address:")
        self.line_phn = QLineEdit()
        self.line_name = QLineEdit()
        self.line_birth_date = QLineEdit()
        self.line_phone = QLineEdit()
        self.line_email = QLineEdit()
        self.line_address = QLineEdit()

        # disable editing on all the lines for layout 2
        self.line_phn.setEnabled(False)
        self.line_name.setEnabled(False)
        self.line_birth_date.setEnabled(False)
        self.line_phone.setEnabled(False)
        self.line_email.setEnabled(False)
        self.line_address.setEnabled(False)

        # buttons and line for layout3
        self.line_set_phn = QLineEdit()
        self.line_set_phn.setPlaceholderText("Enter PHN")
        self.button_set_cur_patient = QPushButton("Set")
        self.button_unset_cur_patient = QPushButton("Unset")

        # control the widths for layout 2
        self.label_cur_patient.setMaximumHeight(15)
        self.line_phn.setMaximumWidth(240)
        self.line_phn.setMinimumWidth(240)
        self.line_name.setMaximumWidth(240)
        self.line_birth_date.setMaximumWidth(240)
        self.line_phone.setMaximumWidth(240)
        self.line_email.setMaximumWidth(240)
        self.line_address.setMaximumWidth(240)

        # control the widths for layout 3
        self.line_set_phn.setMaximumWidth(80)
        self.button_set_cur_patient.setMaximumWidth(80)
        self.button_unset_cur_patient.setMaximumWidth(80)

        # add all the layout2 widgets to layout 2
        layout2.addWidget(self.label_cur_patient, 0, 1)
        layout2.addWidget(self.label_phn, 1, 0)
        layout2.addWidget(self.line_phn, 1, 1)
        layout2.addWidget(self.label_name, 2, 0)
        layout2.addWidget(self.line_name, 2, 1)
        layout2.addWidget(self.label_birth_date, 3, 0)
        layout2.addWidget(self.line_birth_date, 3, 1)
        layout2.addWidget(self.label_phone, 4, 0)
        layout2.addWidget(self.line_phone, 4, 1)
        layout2.addWidget(self.label_email, 5, 0)
        layout2.addWidget(self.line_email, 5, 1)
        layout2.addWidget(self.label_address, 6, 0)
        layout2.addWidget(self.line_address, 6, 1)

        # add all the layout3 widgets to layout3
        layout3.addWidget(self.button_set_cur_patient)
        layout3.addWidget(self.line_set_phn)
        layout3.addWidget(self.button_unset_cur_patient)

        #set the spacing for layout 2
        layout2.setHorizontalSpacing(10)
        layout2.setVerticalSpacing(0)

        # widgets for layout 4
        self.button_logout = QPushButton("Logout")
        self.button_quit = QPushButton("Quit")

        # add layout4 widgets to layout4
        layout4.addWidget(self.button_logout, 0, 0)
        layout4.addWidget(self.button_quit, 1, 0)

        # add layouts 2-4 to the main layout
        self.main_layout.addLayout(layout2, 0, 2)
        self.main_layout.addLayout(layout3, 1, 2)
        self.main_layout.addLayout(layout4, 1, 0)

        self.main_layout.setHorizontalSpacing(25)

        # this is the layout for displaying patient info that can be changed
        self.create_patient_layout = QGridLayout()

        # make all the widgets for create layout
        self.create_patient_layout = QGridLayout()
        self.create_label_phn = QLabel("PHN:")
        self.create_label_name = QLabel("Name:")
        self.create_label_birthdate = QLabel("Birth Date:")
        self.create_label_phone = QLabel("Phone Number:")
        self.create_label_email = QLabel("Email:")
        self.create_label_address = QLabel("Address:")
        self.create_line_phn = QLineEdit()
        self.create_line_phn.setPlaceholderText("Enter patient phn")
        self.create_line_name = QLineEdit()
        self.create_line_name.setPlaceholderText("Enter patient name")
        self.create_line_birthdate = QLineEdit()
        self.create_line_birthdate.setPlaceholderText("Enter Patient birthday")
        self.create_line_phone = QLineEdit()
        self.create_line_phone.setPlaceholderText("Enter patient phone #")
        self.create_line_email = QLineEdit()
        self.create_line_email.setPlaceholderText("Enter patient email")
        self.create_line_address = QLineEdit()
        self.create_line_address.setPlaceholderText("Enter patient address")

        # set the width for the create widgets
        self.create_line_phn.setMaximumWidth(175)
        self.create_line_name.setMaximumWidth(175)
        self.create_line_birthdate.setMaximumWidth(175)
        self.create_line_phone.setMaximumWidth(175)
        self.create_line_email.setMaximumWidth(175)
        self.create_line_address.setMaximumWidth(175)
        self.create_line_phn.setMinimumWidth(175)
        self.create_line_name.setMinimumWidth(175)
        self.create_line_birthdate.setMinimumWidth(175)
        self.create_line_phone.setMinimumWidth(175)
        self.create_line_email.setMinimumWidth(175)
        self.create_line_address.setMinimumWidth(175)

        # add the create widgets to the layout
        self.create_patient_layout.addWidget(self.create_label_phn, 0, 0)
        self.create_patient_layout.addWidget(self.create_label_name, 1, 0)
        self.create_patient_layout.addWidget(self.create_label_birthdate, 2, 0)
        self.create_patient_layout.addWidget(self.create_label_phone, 3, 0)
        self.create_patient_layout.addWidget(self.create_label_email, 4, 0)
        self.create_patient_layout.addWidget(self.create_label_address, 5, 0)
        self.create_patient_layout.addWidget(self.create_line_phn, 0, 1)
        self.create_patient_layout.addWidget(self.create_line_name, 1, 1)
        self.create_patient_layout.addWidget(self.create_line_birthdate, 2, 1)
        self.create_patient_layout.addWidget(self.create_line_phone, 3, 1)
        self.create_patient_layout.addWidget(self.create_line_email, 4, 1)
        self.create_patient_layout.addWidget(self.create_line_address, 5, 1)

        # add the create layout to the main layout
        self.create_patient_layout.setVerticalSpacing(5)
        self.main_layout.addLayout(self.create_patient_layout, 0, 1)

        # show the main layout as the central widget
        widget = QWidget()
        widget.setLayout(self.main_layout)

        self.setCentralWidget(widget)

        # connect all the buttons to their respective functions
        self.button_set_cur_patient.clicked.connect(self.set_cur_patient)
        self.button_unset_cur_patient.clicked.connect(self.unset_cur_patient)
        self.button_quit.clicked.connect(self.quit_button_clicked)
        self.button_logout.clicked.connect(self.logout_button_clicked)
        self.button_create_patient.clicked.connect(self.create_patient_clicked)
        self.button_search_patient.clicked.connect(self.search_patient_clicked)
        self.button_retrieve_patients.clicked.connect(self.retrieve_patients_clicked)
        self.button_delete_patient.clicked.connect(self.delete_patients_clicked)
        self.button_update_patient.clicked.connect(self.update_patient_clicked)
        self.button_list_patients.clicked.connect(self.list_patients_clicked)
        self.button_begin_appointment.clicked.connect(self.begin_appointment_clicked)
        self.button_clear.clicked.connect(self.clear_button_clicked)

    # for when the set current patient button is pressed, sets the given phn as the current patient if valid and displays their info
    def set_cur_patient(self):
        message = QMessageBox(self)
        phn = self.line_set_phn.text()
        try: 
            self.controller.set_current_patient(int(phn))

            patient = self.controller.get_current_patient()
            self.line_phn.setText(str(patient.phn))
            self.line_name.setText(patient.name)
            self.line_birth_date.setText(patient.birth_date)
            self.line_phone.setText(patient.phone)
            self.line_email.setText(patient.email)
            self.line_address.setText(patient.address)
            self.line_set_phn.setText("")
        except:
            message.warning(self, "Patient does not exist", "Please check your input")

    # when the unset button is pressed unsets the current patient and clears their info from the screen
    def unset_cur_patient(self):
            self.controller.unset_current_patient()
            self.line_phn.setText("")
            self.line_name.setText("")
            self.line_birth_date.setText("")
            self.line_phone.setText("")
            self.line_email.setText("")
            self.line_address.setText("")
            self.line_set_phn.setText("")

    # logs the user out and sends them back to the login window
    def logout_button_clicked(self):
        message = QMessageBox(self)
        try: 
            self.controller.logout()
            message.information(self, "Logout Successful!", "Logged out, Goodbye")
            self.login_window = LoginWindow(self.controller, self)
            self.login_window.show()
            self.hide()
        except:
            message.warning(self, "Logout Failed", "Could not logout")
        
    # closes the application
    def quit_button_clicked(self):
        QApplication.quit()

    # creates a patient with all the info from the fields 
    def create_patient_clicked(self):
        phn = self.create_line_phn.text()
        name = self.create_line_name.text()
        birthdate = self.create_line_birthdate.text()
        phone = self.create_line_phone.text()
        email = self.create_line_email.text()
        address = self.create_line_address.text()
        message = QMessageBox(self)
        try:
            self.controller.create_patient(int(phn), name, birthdate, phone, email, address)
            message.information(self, "Success!", " Patient created!")
            self.clear_patient_fields()
        except:
            message.warning(self, "error", "An error occured while creating the patient")

    # searches for a patient with the given phn and displays their info in the fields
    def search_patient_clicked(self):
        phn = self.create_line_phn.text()
        message = QMessageBox(self)
        try:
            patient = self.controller.search_patient(int(phn))

            self.create_line_phn.setText(str(patient.phn))
            self.create_line_name.setText(patient.name)
            self.create_line_birthdate.setText(patient.birth_date)
            self.create_line_phone.setText(patient.phone)
            self.create_line_email.setText(patient.email)
            self.create_line_address.setText(patient.address)
        except:
            message.warning(self, "error", "An error occured while searching for the patient")
            self.clear_patient_fields()

    # opens a new window showing a list of all the patients who match the search criteria from the name field
    def retrieve_patients_clicked(self):
        name = self.create_line_name.text()
        patient_list = self.controller.retrieve_patients(name)

        self.patient_window = PatientTableGUI(self.controller, patient_list, name)
        self.patient_window.show()

    # deletes the patient with the phn from the phn field
    def delete_patients_clicked(self):
        phn = self.create_line_phn.text()
        patient = self.controller.search_patient(phn)
        message = QMessageBox(self)
        if patient:
            dlg = Delete_Dialogue()
            if dlg.exec():
                try:
                    self.controller.delete_patient(int(phn))
                    self.clear_patient_fields()
                    message.information(self, "Patient Deleted", "The Patient was successfully deleted!")
                except:
                    message.warning(self, "Error Deleting Patient", "The patient could not be deleted")
                    self.clear_patient_fields()
        else:
            message.warning(self, "Must Specify phn", "Please specify the phn of the patient you wish to delete")

    # updates the patient information with that from the fields, opens a dialogue to confirm the old phn to allow updating of the phn
    def update_patient_clicked(self):
        self.original_phn = 0
        phn = self.create_line_phn.text()
        name = self.create_line_name.text()
        birthdate = self.create_line_birthdate.text()
        phone = self.create_line_phone.text()
        email = self.create_line_email.text()
        address = self.create_line_address.text()
        message = QMessageBox(self)

        dlg = Update_Dialogue(self.controller, self)
        if dlg.exec():
            try:
                self.controller.update_patient(self.original_phn, phn, name, birthdate, phone, email, address)
                message.information(self, "Patient Updated", "Patient Successfully updated")
                self.clear_patient_fields()
            except:
                message.warning(self, "Error While Updating patient", "An error occured while updating the patient")
                self.clear_patient_fields()

    # creates a new window showing a list of all the patients
    def list_patients_clicked(self):
        patient_list = self.controller.list_patients()

        self.patient_window = PatientTableGUI(self.controller, patient_list, "")
        self.patient_window.show()

    # calls the clear patient fields function 
    def begin_appointment_clicked(self):
        if self.controller.get_current_patient() == None:
            message = QMessageBox(self)
            message.warning(self, "No current patient", "Please set a current patient before starting appointment")
        else: 
            self.layout6 = Noteswindow(self.controller, self)
            self.layout6.show()
            self.hide()

    def clear_button_clicked(self):
        self.clear_patient_fields()
        
    # clears all the patient fields 
    def clear_patient_fields(self):
        self.create_line_phn.setText("")
        self.create_line_name.setText("")
        self.create_line_birthdate.setText("")
        self.create_line_phone.setText("")
        self.create_line_email.setText("")
        self.create_line_address.setText("")


class Noteswindow(QMainWindow):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller  
        self.main_window = main_window   
        self.update_state = 0
        self.update_code = 0

        # layouts, 3 parts: buttton, note edit, list note
        self.setWindowTitle("Notes")
        self.mainlayout = QGridLayout()
        self.button_layout = QVBoxLayout()
        self.note_edit_widget = QPlainTextEdit()
        self.list_note_widget = QPlainTextEdit()
        self.note_edit_widget.setPlaceholderText(
            "Please enter text to create a note\n\nPlease enter text to retrieve notes\n\nPlease enter a note code to update a note\n\nPlease enter a note code to delete a note"
        )
        self.list_note_widget.setEnabled(False)

        # creating buttons for button_layout
        self.button_create_note = QPushButton("Create Note")
        self.button_retrieve_notes = QPushButton("Retrieve Notes")
        self.button_update_note = QPushButton("Update Note")
        self.button_delete_note = QPushButton("Delete Note")
        self.button_list_full_patient_record = QPushButton("List Full Patient Record")
        self.button_end_appointment = QPushButton("End Appointment")
        self.button_clear = QPushButton("Clear")

        # adding button widgets to layout
        self.button_layout.addWidget(self.button_create_note)
        self.button_layout.addWidget(self.button_retrieve_notes)
        self.button_layout.addWidget(self.button_update_note)
        self.button_layout.addWidget(self.button_delete_note)
        self.button_layout.addWidget(self.button_list_full_patient_record)
        self.button_layout.addWidget(self.button_clear)
        self.button_layout.addWidget(self.button_end_appointment)

        # layout positions
        self.mainlayout.addLayout(self.button_layout, 0, 0)
        self.mainlayout.addWidget(self.note_edit_widget, 0, 1)
        self.mainlayout.addWidget(self.list_note_widget, 0, 2)

        # connect all the buttons to their respective functions
        self.button_create_note.clicked.connect(self.create_note)
        self.button_retrieve_notes.clicked.connect(self.retrieve_notes)
        self.button_update_note.clicked.connect(self.update_note)
        self.button_delete_note.clicked.connect(self.delete_note)
        self.button_list_full_patient_record.clicked.connect(self.list_full_patient_record)
        self.button_clear.clicked.connect(self.clear_fields)
        self.button_end_appointment.clicked.connect(self.end_appointment)
        widget = QWidget()
        widget.setLayout(self.mainlayout)
        self.setCentralWidget(widget)

    # create a new note when create note button pressed
    def create_note(self):
        message = QMessageBox(self)
        self.new_note = self.note_edit_widget.toPlainText()
        if self.new_note == "":
            message.warning(self, "Empty input", "Please do not enter an empty message") 
        else:
            try:
                self.controller.create_note(self.new_note)
                message.information(self, "Note Created", "Note successfully created!")
                self.note_edit_widget.setPlainText("")
            except:
                message.warning(self, "Error", "An error occured while creating the note")

    # retrieve all notes with their codes according to the input 
    def retrieve_notes(self):
        self.list_note_widget.setPlainText("")
        text = self.note_edit_widget.toPlainText()
        notes = self.controller.retrieve_notes(text)
        message = QMessageBox(self)
        if notes == []:
            message.information(self, "Notes does not exist", "Patient doesn't have any notes related to this keyword")

        for note in notes:
            display_str = str(note.code) + ": " + note.text
            self.list_note_widget.appendPlainText(display_str)

    # delete the note aaccording to the input code, the code will not be used again if a new note is created
    def delete_note(self):
        dlg = Delete_Note_Dialogue()
        message = QMessageBox(self)
        num = self.note_edit_widget.toPlainText()
        if dlg.exec():
            try:
                note_exist = self.controller.delete_note(int(num))
                self.clear_fields()
                if note_exist == False:
                    message.information(self, "Note does not exist", "Please enter a valid note code")
                else:
                    message.information(self, "Note Deleted", "The note was successfully deleted!")
            except:
                message.warning(self, "Error Deleting Note", "The note could not be deleted")
                self.clear_fields()

    # list all the notes current patient has, if no note     
    def list_full_patient_record(self):
        message = QMessageBox(self)
        try:
            self.list_note_widget.setPlainText("")
            notes = self.controller.list_notes()
            for note in notes:
                display_str = str(note.code) + ": " + note.text
                self.list_note_widget.appendPlainText(display_str)
            if notes == []:
                message.information(self, "Notes does not exist", "Patient doesn't have any notes yet")
        except:
            message.warning(self, "Notes does not exist", "Patient doesn't have any notes yet")

    def update_note(self):
        message = QMessageBox(self)
        if self.update_state == 0:      # if update state is 0 then the button is expecting an int in the text box
            try:            
                self.update_code = int(self.note_edit_widget.toPlainText())
                note = self.controller.search_note(self.update_code)
                dlg = Update_Note_Dialogue()
                if dlg.exec():
                    self.note_edit_widget.setPlainText(note.text)
                    self.update_state = 1
                else:
                    self.note_edit_widget.setPlainText("")
                    self.update_code = 0
                    self.update_state = 0
            except:
                message.warning(self, "Error Updating Note", "An error occured while updating the note")
                self.update_code = 0
                self.update_state = 0
                self.note_edit_widget.setPlainText("")

        elif self.update_state == 1:    # if update state is 1 the the button has been pressed once and now the button is expecting text
            try:
                new_text = self.note_edit_widget.toPlainText()
                self.controller.update_note(self.update_code, new_text)
                self.note_edit_widget.setPlainText("")
                self.update_code = 0
                self.update_state = 0
            except:
                message.warning(self, "Error Updating Note", "An error occured while updating the note")
                self.update_code = 0
                self.update_state = 0
                self.note_edit_widget.setPlainText("")

    def clear_fields(self):
        self.list_note_widget.setPlainText("")
        self.note_edit_widget.setPlainText("")

    def end_appointment(self):
        self.close()

    def closeEvent(self, a0):
        self.main_window.show()
        return super().closeEvent(a0)


def main():
    app = QApplication(sys.argv)
    window = ClinicGUI()
    #window.show()
    app.exec()

if __name__ == '__main__':
    main()

