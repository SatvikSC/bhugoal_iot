#!/usr/bin/python

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from time import sleep

#i2c = busio.I2C(board.SCL,board.SDA)
i2c = busio.I2C(3,2)
ads = ADS.ADS1115(i2c)

for _ in range(1,11):
    chan = AnalogIn(ads,ADS.P1)
    print(round(chan.voltage,5), round(chan.voltage*6))
    sleep(1)
