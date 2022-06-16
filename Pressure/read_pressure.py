#!/usr/bin/python

import Adafruit_BMP.BMP085 as BMP085
import time


time.sleep(1)
bmp = BMP085.BMP085()

pressure = bmp.read_pressure()
sealevel_pressure = bmp.read_sealevel_pressure()

if pressure is not None:
    print('P = {0:0.2f} Pa  C.L. P = {0:0.2f} Pa'.format(pressure, sealevel_pressure))
else:
    print('Fail to read. Try again!')
