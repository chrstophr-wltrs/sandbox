import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic

Ui_LoginForm, baseClass = uic.loadUiType('loginbox.ui')

class MainWindow(baseClass):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
