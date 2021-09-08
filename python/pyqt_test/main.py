import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import random as rnd

class MainWindow(qtw.QWidget):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        self.number_label = qtw.QLabel('00,000')
        self.generate_button = qtw.QPushButton('Generate')
        self.generate_button.clicked.connect(self.generate_big_number)
        
        layout = qtw.QVBoxLayout()
        layout.addWidget(self.number_label)
        layout.addWidget(self.generate_button)
        self.setLayout(layout)
        self.show()
    
    def generate_big_number(self):
        self.number_label.setText(f"{rnd.randint(10000, 99999):,}")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
