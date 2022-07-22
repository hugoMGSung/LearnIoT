# qsignalslot_exam
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QPushButton,
                               QLabel, QVBoxLayout, QDial)

class qdial_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.dial1 = QDial(self)
        self.dial1.move(30, 10)
        self.dial1.valueChanged.connect(self.changeValue)
        
        self.dial2 = QDial(self)
        self.dial2.move(200, 10)
        self.dial2.setRange(0, 100)
        self.dial2.setNotchesVisible(True)
        self.dial2.valueChanged.connect(self.changeValue)
        
        self.lbl1 = QLabel('다이얼 1 :  0', self)
        self.lbl1.move(37, 130)
        self.lbl1.setFixedSize(200, 30)
        self.lbl2 = QLabel('다이얼 2 :  0', self)
        self.lbl2.move(200, 130)
        self.lbl2.setFixedSize(200, 30)
        
        self.btn = QPushButton('Reset', self)
        self.btn.move(115, 200)
        self.btn.clicked.connect(self.btnClicked)
        
        self.setGeometry(300, 200, 320, 230)
        self.setWindowTitle('QDial!!')
        self.show()
        
    def btnClicked(self):
        self.dial1.setValue(0)
        self.dial2.setValue(0)
        
    def changeValue(self):
        self.lbl1.setText(f'다이얼 1 :{self.dial1.value():>3}')
        self.lbl2.setText(f'다이얼 2 :{self.dial2.value():>3}')
    
app = QApplication(sys.argv)
instance = qdial_exam()

app.exec_()