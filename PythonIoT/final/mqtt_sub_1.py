import time
import paho.mqtt.client as paho

broker='localhost'

#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    recvData = str(message.payload.decode('utf-8'))
    print('received message =', recvData)

client = paho.Client()
client.on_message = on_message

print('connecting to broker ', broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print('subscribing ')
client.subscribe('home/device/fakedata/')#subscribe
time.sleep(5)
client.disconnect() #disconnect
client.loop_stop() #stop loop
time.sleep(10)