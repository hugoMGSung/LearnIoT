from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(320, 230)
    window.setWindowTitle("PyQt5 app")

    label = QLabel('Hello PyQt5!!', window)
    label.move(110, 100)

    window.show()
    app.exec_()