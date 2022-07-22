import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
form_class = uic.loadUiType('./day7/signalslot.ui')[0]

#메인 윈도우 클래스
class WindowClass(QMainWindow, form_class) :
    #초기화
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.initWidget()
        self.show()

    def initWidget(self):
        self.dial.valueChanged.connect(self.lcd.display)
        self.btn1.clicked.connect(self.resizeBig)
        self.btn2.clicked.connect(self.resizeSmall)
    
    def resizeBig(self):
        self.resize(800, 747)

    def resizeSmall(self):
        self.resize(300, 280)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = WindowClass()
    app.exec_()
