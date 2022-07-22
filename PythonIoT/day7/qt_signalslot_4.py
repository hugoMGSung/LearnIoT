import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class WindowClass(QWidget):
    closeSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Close Demo2')
        self.resize(300, 280)

        button = QPushButton('close', self)
        button.clicked.connect(self.onClicked)
        self.closeSignal.connect(self.onClose)
        self.show()

    # Custom Slot Function
    def onClicked(self):
        self.closeSignal.emit()  # Send Custom Signal

    # Custom Slot Function
    def onClose(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = WindowClass()

    sys.exit(app.exec_())