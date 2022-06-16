#!/usr/bin/python


import sys
import time
import Adafruit_BMP.BMP085 as BMP
import Adafruit_DHT as AM2305


time.sleep(1)
Device=22
Pin=22

_, temp_dht = AM2305.read_retry(Device, Pin)

try:
    bmp = BMP.BMP085()
    temp = temp_dht+ bmp.read_temperature()
except Exception as e:
    temp = temp_dht
    
if temp is not None:
    print('Temperature={0:0.1f}*C '.format(temp))
else:
    print('Fail to read. Try again!')
