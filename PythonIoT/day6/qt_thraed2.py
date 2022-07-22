import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time

#UI파일 연결
form_class = uic.loadUiType('./day6/ui/thread_ui1.ui')[0]

# 스레드 
class CountThread(QThread):
    def __init__(self, parent) -> None: # parent는 WindowClass의 인스턴스
        super().__init__(parent)
        self.parent = parent # self.parent를 사용, WindowClass 위젯 제어가능
        
    def run(self):
        self.parent.pgbTask.setRange(0, 99999) # 99 ~ 99999 까지 변경
        for i in range(0, 10000): # 100 ~ 100000 까지 변경
            print(f"출력 : {str(i)}")
            self.parent.pgbTask.setValue(i) #pgbTask bar 진행률 올리기
            self.parent.txbLog.append("출력 : "+str(i)) #text browser 문자열 추가하기
            time.sleep(0.001)

#메인 윈도우 클래스
class WindowClass(QMainWindow, form_class) :
    #초기화
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #btnStart를 클릭하면 procCount 시작
        self.btnStart.clicked.connect(self.actionThraed) 
        
        self.show()

    # 시작버튼을 눌렀을 때 스레드처리 함수
    def actionThraed(self):
        th = CountThread(self)
        th.start()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWin = WindowClass()
    app.exec_()