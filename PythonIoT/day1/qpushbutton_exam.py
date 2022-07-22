import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtCore import Qt

class qpushbutton_exam(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):
        btn1 = QPushButton(self); btn1.setText('BUTTON'); btn1.setEnabled = True
        btn2 = QPushButton('&Button2', self); btn2.setEnabled = False
        btn3 = QPushButton('Button3', self); btn3.setFixedSize(200, 70)
        btn3.setIcon(QIcon('./day1/images/lion.png'))
        
        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        
        self.setLayout(hbox)        
        self.setGeometry(300, 200, 320, 230)
        self.setWindowTitle('QPushButton!!')
        self.show()
        
loop = QApplication(sys.argv)
instance = qpushbutton_exam()
loop.exec_()