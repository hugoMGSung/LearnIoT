import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal

class MyMain(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        self.txtline = MyTextLine()
        self.txtline2 = QLineEdit()
        vbox.addWidget(self.txtline)
        vbox.addWidget(self.txtline2)
        self.setLayout(vbox)
        
        self.txtline.A_pressed.connect(self.a_press)  # custom signal - slot 연결함.
        self.show()
        
    @pyqtSlot()
    def a_press(self):
        txt = self.txtline2.text()
        self.txtline2.setText(txt + "A...")
        
class MyTextLine(QLineEdit):
    A_pressed = pyqtSignal()  # custom signal 생성함
        
    def __init__(self, *args):
        super().__init__(*args)
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_A:
            self.A_pressed.emit()  # custom signal 발생
            super().keyPressEvent(e)
        else:
            super().keyPressEvent(e)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyMain()
        
    sys.exit(app.exec_())