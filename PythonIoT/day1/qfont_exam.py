import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class qfont_exam(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 200, 320, 230)
        self.setWindowTitle('QFont!!')
        self.text = 'What the F*!!'
        self.show()
        
    def paintEvent(self, event) -> None:
        paint = QPainter()
        paint.begin(self)
        self.drawText(event, paint)
        paint.end()
    
    def drawText(self, event, paint):
        paint.setPen(QColor(10,10,10))
        paint.setFont(QFont('NanumGothic', 10))
        paint.drawText(105, 100, 'HELL WORLD')
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)
        
        
loop = QApplication(sys.argv)
instance = qfont_exam()
loop.exec_()