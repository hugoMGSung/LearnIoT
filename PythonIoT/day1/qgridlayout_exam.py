import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class qgridlayout_exam(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):
        newBtn = QPushButton('new')
        editBtn = QPushButton('edit')
        delBtn = QPushButton('del')
        searchBtn = QPushButton('search')
        pupBtn = QPushButton('page up')
        pdnBtn = QPushButton('page down')
        
        grid = QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(newBtn, 0, 0)
        grid.addWidget(editBtn, 0, 1)
        grid.addWidget(delBtn, 0, 2)
        grid.addWidget(searchBtn, 1, 0)
        grid.addWidget(pupBtn, 1, 1)
        grid.addWidget(pdnBtn, 1, 2)
        
        self.setLayout(grid)        
        self.setGeometry(300, 200, 320, 230)
        self.setWindowTitle('QGridLayout!!')
        self.show()
        
loop = QApplication(sys.argv)
instance = qgridlayout_exam()
loop.exec_()