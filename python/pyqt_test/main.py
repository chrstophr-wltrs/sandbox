from PyQt5 import QtWidgets as qtw

app = qtw.QApplication([])

w = qtw.QWidget(windowTitle = 'hello world')

if __name__ == "__main__":
    w.show()
    app.exec_()
