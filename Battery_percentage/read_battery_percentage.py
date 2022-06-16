#!/usr/bin/python

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from time import sleep

#i2c = busio.I2C(board.SCL,board.SDA)
i2c = busio.I2C(3, 2)
ads = ADS.ADS1115(i2c)
r1 = 11000
r2 = 1000

for _ in range(1, 11):
    chan = AnalogIn(ads, ADS.P2)
    voltage = round(chan.voltage, 5)
    main_volt = voltage / (r2 / (r1 + r2))

    if main_volt >= 12.7:
        battery = 100
    elif main_volt in range(12.60, 12.71):
        battery = 95
    elif main_volt in range(12.50, 12.60):
        battery = 90
    elif main_volt in range(12.42, 12.50):
        battery = 80
    elif main_volt in range(12.32, 12.42):
        battery = 70
    elif main_volt in range(12.20, 12.32):
        battery = 60
    elif main_volt in range(12.06, 12.20):
        battery = 50
    elif main_volt in range(11.90, 12.06):
        battery = 40
    elif main_volt in range(11.75, 11.90):
        battery = 30
    elif main_volt in range(11.58, 11.75):
        battery = 20

    if battery >= 20:
        print("Battery Percentage: {}%".format(battery))
    else:
        print("Danger !!")

    sleep(1)
