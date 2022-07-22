import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class WindowClass(QWidget):
    closeSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Close Demo")
        self.resize(300, 280)

        button = QPushButton("close", self)
        button.clicked.connect(self.onClose)
        self.closeSignal.connect(self.close) # 커스텀 시그널에 연결
        self.show()

    def onClose(self):
        self.closeSignal.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = WindowClass()

    sys.exit(app.exec_())