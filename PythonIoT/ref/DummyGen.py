'''
2022-05-20
DummyGen.py 
이전 C#으로 개발한 DummyGen을 Python으로 이전 
'''
import threading
import datetime as dt
import paho.mqtt.client as mqtt
import json
import random as rnd

client2 = None
count = 0
rooms = ('DiningRoom', 'LivingRoom', 'BathRoom', 'BedRoom', 'GuestRoom')

'''
{
  "Dev_Id": "DiningRoom",
  "Curr_Time": "2022-05-24 15:57:27.80",
  "Temp": 23.37,
  "Humid": 44.4,
  "Press": 844.5
}
형태로 json 파일을 만들어야 함
'''
def generate_dummy_data():
    global rooms
    rnd_room = rnd.choice(rooms)
    rnd_temp = round(rnd.uniform(20.1, 25.9), 2)
    rnd_humid = round(rnd.uniform(40.1, 49.9), 2)
    rnd_press = round(rnd.uniform(400.1, 900.9), 2)
    
     
    curr = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    gen_origin = { 'Dev_Id' : rnd_room, 'Curr_Time' : curr, 'Temp' : rnd_temp,
                   'Humid' : rnd_humid, 'Press' : rnd_press }
    pub_data = json.dumps(gen_origin)
    
    client2.publish('home/device/data/', pub_data)
    print(f'Published : {pub_data}')
    
    threading.Timer(3.0, generate_dummy_data).start()
    
if __name__ == '__main__':
    mqtt_broker_url = 'localhost'
    client2 = mqtt.Client('DummyPublisher')
    client2.connect(mqtt_broker_url)
    
    generate_dummy_data()