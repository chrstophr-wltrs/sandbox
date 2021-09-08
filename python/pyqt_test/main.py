from PyQt5 import QtWidgets as qtw

app = qtw.QApplication([])

w = qtw.QWidget(windowTitle = 'hello world')

def main():
    w.show()
    app.exec_()

if __name__ == "__main__":
    main()
