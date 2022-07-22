import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class qwidget_exam(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):
        btn01 = QPushButton('Click', self)
        btn01.setGeometry(50, 100, 100, 40)
        #btn01.move(100, 150)
        # btn01.resize(120, 50)
        #btn01.setText('Click Me')
        
        
        self.setGeometry(300, 200, 320, 230)
        self.setWindowTitle('QWidget!!')
        self.show()
        
loop = QApplication(sys.argv)
instance = qwidget_exam()
loop.exec_()