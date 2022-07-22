from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication, QWidget, QLabel
import sys

QCoreApplication.setLibraryPaths(['C:/DEV/Langs/Python/Python310/Lib/site-packages/PySide2/plugins'])

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(320, 230)
    window.setWindowTitle("PySide2 app")

    label = QLabel('Hello PySide2!!', window)
    label.move(110, 100)

    window.show()
    app.exec_()