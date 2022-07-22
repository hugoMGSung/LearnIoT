import sys
from PySide2.QtWidgets import (QApplication, QWidget, QPushButton, 
                               QMessageBox)

class qmessagebox_exam(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):        
        self.btn1 = QPushButton('프로그램 종료', self)
        self.btn1.move(190, 180)
        self.btn1.setFixedSize(120, 35)
        self.btn1.clicked.connect(self.close)
        
        self.setGeometry(300, 200, 320, 230)
        self.setWindowTitle('QInputDialog!!')
        self.show()
        
    def close(self):
        q = QMessageBox.question(self, '종료', \
                '종료하시겠습니까?', \
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if q == QMessageBox.Yes: super().close()
        
app = QApplication(sys.argv)
instance = qmessagebox_exam()

app.exec_()