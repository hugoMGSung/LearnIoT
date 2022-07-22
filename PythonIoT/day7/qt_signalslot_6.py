import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time

#UI파일 연결
form_class = uic.loadUiType('./day7/signalslot2.ui')[0]

#메인 윈도우 클래스
class MyMain(QMainWindow, form_class):
    add_sec_signal = pyqtSignal()
    send_instance_singal = pyqtSignal('PyQt_PyObject')
    
    #초기화
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.initWidget()
        self.show()
        
    def initWidget(self):
        self.btnStart.clicked.connect(self.time_start)
        self.btnStop.clicked.connect(self.time_stop)
        self.btnAddNum.clicked.connect(self.add_sec)
        self.btnSendInstance.clicked.connect(self.send_instance)
        self.myThread = Worker(parent=self)
        
        self.myThread.sec_changed.connect(self.time_update)  # 워커 스레드로부터 메인 스레드로 보내는 커스텀 시그널
        self.add_sec_signal.connect(self.myThread.add_sec)   # 메인 스레드로부터 워커 스레드로 보내는 커스텀 시그널
        self.send_instance_singal.connect(self.myThread.recive_instance_singal)
        
    @pyqtSlot()
    def time_start(self):
        self.myThread.start()
        self.myThread.working = True
        
    @pyqtSlot()
    def time_stop(self):
        self.myThread.working = False
        
    @pyqtSlot()
    def add_sec(self):
        print(".... add singal emit....")
        self.add_sec_signal.emit()

    @pyqtSlot(str)
    def time_update(self, msg):
        self.txtLog.append(msg)
        
    @pyqtSlot()
    def send_instance(self):
        t1 = Test()
        t1.name = "SuperPower!!!"
        self.send_instance_singal.emit(t1)
        
class Test:
    def __init__(self):
        name = ""
        
class Worker(QThread):
    sec_changed = pyqtSignal(str)
    
    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.working = True
        self.sec = sec
        
    def __del__(self):
        print(".... end thread.....")
        self.wait()
        
    def run(self):
        while self.working:
            self.sec_changed.emit('time (secs)：{}'.format(self.sec))
            time.sleep(0.01)
            self.sec += 1
            
    @pyqtSlot()
    def add_sec(self):
        print("add_sec....")
        self.sec += 10000000
        
    @pyqtSlot("PyQt_PyObject")    # @pyqtSlot(object) 도 가능..
    def recive_instance_singal(self, inst):
        print(inst.name)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyMain()
    app.exec_()