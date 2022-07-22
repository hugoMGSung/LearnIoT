## HMI 시작
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import datetime
import time
import sys
import json

import paho.mqtt.client as mqtt

broker = '127.0.0.1'
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class Worker(QThread):
    mqtt_messages = pyqtSignal(dict)
    mqtt_status = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.HOST = '127.0.0.1'
        self.PORT = 1883
        self.client = mqtt.Client()
    
    def on_connect(self, mqttc, obj, flags, rc):
        print(f'Connected with result code {str(rc)}')
        self.mqtt_status.emit('MQTT CONNECTED')
  
    def on_message(self, mqttc, obj, msg):
        recv_msg = str(msg.payload.decode('utf-8'))
        print(f'{msg.topic} : {recv_msg}')
        result = json.loads(recv_msg)
        self.mqtt_messages.emit(result)
        
        time.sleep(1)
    
    def mqttloop(self):
        self.client.loop()
        print('MQTT module tick')
        
    def run(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.HOST, self.PORT, 60)
        self.client.subscribe('home/device/#')            
        self.client.loop_forever()

#UI파일 연결
form_class = uic.loadUiType('./hmi_window.ui')[0]

class Dashboard(QMainWindow, form_class):
    # 초기화 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showtime()
        
        self.btnStart.clicked.connect(self.thread_start)
        # self.dial_temp.valueChanged.connect(self.lbl_temp_val.text())
        
        self.myThread = Worker(parent=self)
        self.myThread.mqtt_messages.connect(self.update_table_widget)
        self.myThread.mqtt_status.connect(self.update_status)
        self.show()
        
    @pyqtSlot()
    def thread_start(self):
        self.myThread.start()
        self.myThread.working = True
    
    @pyqtSlot(str)
    def update_status(self, msg):
        self.lbl_mqtt_stat.setText(msg)
        
    @pyqtSlot(dict)
    def update_table_widget(self, data):
        res = json.dumps(data)
        print(int(data["Temp"]))
        print(int(data["Humid"]))
        self.lbl_temp_val.setText(str(int(data["Temp"])))
        self.lbl_humid_val.setText(str(int(data["Humid"])))
        self.dial_temp.setValue(int(data["Temp"]))
        self.dial_humid.setValue(int(data["Humid"]))
        self.txtResult.append(res)
        
    def showtime(self):
        curr_time = QTime.currentTime()
        today = QDateTime.currentDateTime()
        ind = datetime.today().weekday()
        self.lbl_date.setText(today.toString("yyyy-MM-dd"))
        self.lbl_day.setText(days[ind])
        self.lbl_time.setText(curr_time.toString('HH:mm'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Dashboard()
    sys.exit(app.exec_())
