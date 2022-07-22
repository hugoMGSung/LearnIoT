import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time

#UI파일 연결
form_class = uic.loadUiType('./day6/ui/thread_ui1.ui')[0]

#메인 윈도우 클래스
class WindowClass(QMainWindow, form_class) :
    #초기화
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initWidget()
        
        self.show()
        
    def initWidget(self):
        self.btnStart.clicked.connect(self.thread_start)
        self.myThread = Worker(parent=self)        
        self.myThread.num_changed.connect(self.update_display)  # 워커 스레드로부터 메인 스레드로 보내는 커스텀 시그널
        self.myThread.set_progressTask.connect(self.update_progress)  # 워커 스레드로부터 메인 스레드로 보내는 커스텀 시그널

    @pyqtSlot()
    def thread_start(self):
        self.pgbTask.setRange(0, 9999) # 99 ~ 99999 까지 변경
        self.myThread.start()
        self.myThread.working = True
    
    @pyqtSlot(str)
    def update_display(self, msg):
        self.txbLog.append(msg)
        
    @pyqtSlot(int)
    def update_progress(self, value):
        self.pgbTask.setValue(value)
        if value == 9999:
            self.myThread.working = False

class Worker(QThread):
    num_changed = pyqtSignal(str)
    set_progressTask = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.working = True
        
    def run(self):
        while self.working:
            for i in range(0, 10000): # 100 ~ 100000 까지 변경
                print(f"출력 : {str(i)}")
                self.set_progressTask.emit(i)
                self.num_changed.emit(f'출력 : {str(i)}')
                time.sleep(0.0001)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWin = WindowClass()
    app.exec_()