import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
                               QPushButton, QHBoxLayout, QVBoxLayout, QInputDialog)
from PySide2.QtGui import QIcon, QFont, QFontDatabase
from PySide2.QtCore import Qt

class qinputdlg_exam(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.day = ['월','화','수','목','금']
        self.initUI()
        
    def initUI(self):        
        self.btn1 = QPushButton('일자', self)
        self.btn1.move(50, 25)
        self.btn1.setFixedSize(120, 35)
        self.btn1.clicked.connect(self.showDialog1)
        
        self.label1 = QLabel('일자입력', self)
        self.label1.move(180, 33)
        self.label1.setFixedSize(180, 20)
        
        self.setGeometry(300, 200, 320, 230)
        self.setWindowTitle('QInputDialog!!')
        self.show()
        
    def showDialog1(self):
        text, flag = QInputDialog.getInt(self, '일자선택', '일자를 선택하세요', \
                                        min=1, max=31)
        if flag:
            self.label1.setText(f'{str(text)}일')
        # text, flag = QInputDialog.getText(self, '입력', '이름을 입력하세요')
        # if flag:
        #     self.label1.setText(text)
        
app = QApplication(sys.argv)
instance = qinputdlg_exam()

app.exec_()