import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        self.username_input = qtw.QLineEdit()
        self.password_input = qtw.QLineEdit()
        self.password_input.setEchoMode(
            qtw.QLineEdit.Password)

        self.login_button = qtw.QPushButton('Login')
        self.cancel_button = qtw.QPushButton('Cancel')

        layout = qtw.QFormLayout()
        layout.addRow('Username:', self.username_input)
        layout.addRow('Password:', self.password_input)

        button_widget = qtw.QWidget()
        button_widget.setLayout(qtw.QHBoxLayout())
        button_widget.layout().addWidget(self.login_button)
        button_widget.layout().addWidget(self.cancel_button)
        
        self.cancel_button.clicked.connect(self.close)
        self.login_button.clicked.connect(self.authenticate)

        layout.addWidget(button_widget)

        self.setLayout(layout)
        self.show()

    def authenticate(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == 'user' and password == 'pass':
            qtw.QMessageBox.information(self, 
                                        'Success', 
                                        'You are logged in!')
        else:
            qtw.QMessageBox.critical(self,
                                    'Failed',
                                    'Invalid login credentials, please try again.')

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
