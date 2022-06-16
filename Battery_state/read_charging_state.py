#!/usr/bin/python

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from time import sleep

#i2c = busio.I2C(board.SCL,board.SDA)
i2c = busio.I2C(3, 2)
ads = ADS.ADS1115(i2c)
r1 = 12000
r2 = 2200

for _ in range(1, 11):
    chan = AnalogIn(ads, ADS.P3)
    voltage = round(chan.voltage, 5)
    main_volt = voltage / (r2 / (r1 + r2))

    if main_volt > 8:
        print("Charging")
    else:
        print("Not Charging")

    sleep(1)
