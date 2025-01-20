import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout
from PyQt6.QtWidgets import QTableView, QPlainTextEdit, QDialog

from clinic.controller import Controller

# shown when first opening the program, asks user to login or quits the program
class LoginWindow(QWidget):
    def __init__(self, controller, parent_window):
        super().__init__()

        self.controller = controller
        self.parent_window = parent_window
        self.setWindowTitle("Login")

        # set the layout for the login window
        layout = QGridLayout()

        label_username = QLabel("Username")
        self.text_username = QLineEdit()
        label_password = QLabel("Password")
        self.text_password = QLineEdit()
        self.text_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.button_login = QPushButton("Login")
        self.button_logout = QPushButton("Logout")
        self.button_quit = QPushButton("Quit")

        layout.addWidget(label_username, 0, 0)
        layout.addWidget(self.text_username, 0, 1)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.text_password, 1, 1)
        layout.addWidget(self.button_login, 2, 0)
        layout.addWidget(self.button_logout, 2, 1)
        layout.addWidget(self.button_quit, 2, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setLayout(layout)

        # connect the buttons' clicked signals to the slots below
        self.button_login.clicked.connect(self.login_button_clicked)
        self.button_logout.clicked.connect(self.logout_button_clicked)
        self.button_quit.clicked.connect(self.quit_button_clicked)

    # Attmepts to log the user in with given password and username
    def login_button_clicked(self):
        username = self.text_username.text()
        password = self.text_password.text()

        message = QMessageBox(self)
        try:
            self.controller.login(username, password)
            message.information(self, "Login Successful!", "Logged in, Welcome")
            self.parent_window.show()
            self.close()
        except:
            message.warning(self, "Login Failed", "Invalid username or password, please try again")
		
        self.text_username.setText("")
        self.text_password.setText("")

    # logs the user out, This should never actually happen but this was left in incase the login window is somehow open while the user is logged in
    def logout_button_clicked(self):

        message = QMessageBox(self)

        try: 
            self.controller.logout()
            message.information(self, "Logout Successful!", "Logged out, Goodbye")
        except:
            message.warning(self, "Logout Failed", "Could not logout")
        
        self.text_username.setText("")
        self.text_password.setText("")
        
    # quits the program
    def quit_button_clicked(self):
        QApplication.quit()