'''
Publish와 Subscribe가 동시에 되는 MQTT 예제
'''
import threading
import time
import paho.mqtt.client as mqtt
import json

topic = 'data'
broker = '127.0.0.1'  #"test.mosquitto.org"
port = 1883

## 접속함수
def on_connect(client, userdata, flags, rc):
    print('Broker connection succeed -- ')
    print(f'Connected with result code: {str(rc)}')
    client.subscribe(topic) ## SUBSCRIBE 코드 변경 필요
    print(f'Subscribing to topic : {topic}')

## 모든 메시지 확인 함수
def on_message(client, userdata, message):
    print(f'Data requested {str(message.payload)}')


def publishing():
    print(f'WAIT for max: {2}')
    while True:
        time.sleep(1)
        client.publish(topic, 'dfdfd')

### MQTT ###
client = mqtt.Client()
client.connect(broker, port)
client.on_connect = on_connect
#client.on_disconnect = on_disconnect

#
def subscribing():
    client.on_message = on_message
    client.loop_forever()
    
sub = threading.Thread(target=subscribing)
pub = threading.Thread(target=publishing)

### Start MAIN ###
sub.start()
pub.start()