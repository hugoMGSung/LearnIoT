# qsignalslot_exam
import sys
from PySide2.QtWidgets import (QApplication, QWidget, QPushButton,
                               QLabel, QVBoxLayout)

class qsignalslot_exam(QWidget):
    count = 0
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):        
        self.btn = QPushButton('Click')
        self.btn.clicked.connect(self.changeCount)
        
        self.label = QLabel(f'{self.count} 번 눌렀습니다')
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btn)
        self.setLayout(self.vbox)
        
        self.setGeometry(300, 200, 320, 230)
        self.setWindowTitle('QSignal&Slot!!')
        self.show()
    
    def changeCount(self):
        self.count += 1
        self.label.setText(f'{self.count} 번 눌렀습니다')
        
app = QApplication(sys.argv)
instance = qsignalslot_exam()

app.exec_()