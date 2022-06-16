#!/usr/bin/python

import sys
import Adafruit_DHT

Device=22
Pin=22

hum, _ = Adafruit_DHT.read_retry(Device, Pin)

if hum is not None:
    print('Humidity={0:0.1f}%'.format(hum))
else:
    print('Fail to read. Try again!')
