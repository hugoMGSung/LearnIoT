#!/usr/bin/env python

import paho.mqtt.client as mqtt
import smbus2
import bme280
import json
import time
import datetime as dt
import uuid
from collections import OrderedDict

count = 0

try:
    #uuid generating
    def_id = "HUGO01"
    div_uid = uuid.uuid3(uuid.NAMESPACE_OID, def_id)

    #mqtt publisher
    broker_address = "192.168.200.126"
    client2 = mqtt.Client("TempressurClient")
    client2.connect(broker_address)

    #bme280 initialized
    port = 1
    address = 0x76
    bus = smbus2.SMBus(port)

    bme280.load_calibration_params(bus, address)

    while True:
        count += 1        
        currtime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        # 센서값 가져오기
        data = bme280.sample(bus, address)
        # groupdata 만들기
        raw_data = OrderedDict()

        raw_data["uuid"] = def_id
        raw_data["time"] = currtime
        raw_data["temperature"] = data.temperature
        raw_data["pressure"] = data.pressure
        raw_data["humidity"] = data.humidity

        pub_data = json.dumps(raw_data, ensure_ascii=False, indent="\t")

        #mqtt published
        print(div_uid, pub_data)
        client2.publish("home/sensor1/data/", pub_data)

        time.sleep(5)

except Exception as ex:
    print('Error raised ', ex)



