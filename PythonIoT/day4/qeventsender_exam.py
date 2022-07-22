# qeventsender_exam
from ctypes import alignment
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QPushButton,
                               QLabel, QVBoxLayout, QHBoxLayout)
from PySide2.QtCore import Qt

class qeventsender_exam(QWidget):    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.btn1 = QPushButton('Button 01')
        self.btn1.clicked.connect(self.buttonClicked)
        self.btn2 = QPushButton('Button 02')
        self.btn2.clicked.connect(self.buttonClicked)
        self.lbl1 = QLabel('시그널 송신자')
        
        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)
        self.vbox.addWidget(self.lbl1, alignment=Qt.AlignCenter)
        
        self.setGeometry(300, 200, 320, 230)
        self.setWindowTitle('Event Sender!!')
        self.show()
        
    def buttonClicked(self):
        sender = self.sender()
        self.lbl1.setText(f'시그널 송신자 : {sender.text()}')
    
app = QApplication(sys.argv)
instance = qeventsender_exam()

app.exec_()