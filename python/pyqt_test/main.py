from PyQt5.QtWidgets import *

app = QApplication([])

w = QWidget(windowTitle = 'hello world')

def main():
    w.show()
    app.exec_()

if __name__ == "__main__":
    main()
