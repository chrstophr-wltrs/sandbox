import sys

import pandas as pnd
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from numberModule import generateBigNumber


class MainWindow(qtw.QWidget):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        self.number_label = qtw.QLabel('00,000')
        self.generate_button = qtw.QPushButton('Generate')
        self.generate_button.clicked.connect(self.set_label_to_number)
        
        layout = qtw.QVBoxLayout()
        layout.addWidget(self.number_label)
        layout.addWidget(self.generate_button)
        self.setLayout(layout)
        self.show()
    
    def set_label_to_number(self):
        self.number_label.setText(generateBigNumber())

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
