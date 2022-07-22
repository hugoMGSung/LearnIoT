import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class qlabel_exam(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):
        label1, label2 = QLabel(), QLabel()
        label1.setStyleSheet(
            ('border-width: 2px;'
             'border-style: solid;'
             'border-color: blue;'
             'image: url(./images/image1.png)'
            )            
        )
        label2.setStyleSheet(
            ('border-width: 4px;'
             'border-style: dot-dot-dash;'
             'border-color: red;'
             'image: url(./images/image2.png)'
            )            
        )
        
        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(label2)    
            
        self.setLayout(hbox)        
        self.setGeometry(300, 200, 320, 230)
        self.setWindowTitle('QLabel!!')
        self.show()
        
loop = QApplication(sys.argv)
instance = qlabel_exam()
loop.exec_()