#!/usr/bin/env python
import Adafruit_DHT
import datetime
import time
import urllib.request
import pymysql

sensor = Adafruit_DHT.DHT11
pin = 18

print('Reading Temperature&Humidity')

#DB저장
conn = pymysql.connect(host='192.168.200.117', user='root', password='mysql_p@ssw0rd', db='shopdb', charset='utf8')

try:	
	while True:
		wtime = datetime.datetime.now()
		humid, temp = Adafruit_DHT.read_retry(sensor, pin)
	
		if humid is not None and temp is not None:
			print(wtime, 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temp, humid))
		
			curs = conn.cursor()
			query = """INSERT INTO shopdb.testmachine_env (currents_time, machine_num, temperature, humidity) """ \
			        """ VALUES (%s, %s, %s, %s) """
			data = (wtime.strftime("%Y-%m-%d %H:%M:%S"), 119023, temp, humid)
			curs.execute(query, data)
			conn.commit()
		
			time.sleep(10)
		else:
			print('Failed to get readming. Try again!')

finally:
	curs.close()
	conn.close()
