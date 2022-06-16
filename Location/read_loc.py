#!/usr/bin/python

import serial
import time
from decimal import *
from subprocess import call


# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1)
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key


def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i

def sending_cmd_to_gps(cmd):
    port.write(cmd[0].encode())
    rcv = port.read(cmd[1])
    print(rcv)
    time.sleep(.1)


'''
port.write(b'AT;\r\n')
rcv = port.read(100)
print(rcv)
time.sleep(.1)

AT;\r\n                 # To Check the status of the GPS
AT+CGNSPWR=1;\r\n       # To Power the GPS
AT+CGNSIPR=115200;\r\n  # Set the baud rate of GPS
AT+CGNSTST=1;\r\n       # Send data received to UART
AT+CGNSINF;\r\n         # Print the GPS information

'''
CMD=[['AT;\r\n',100],
['AT+CGNSPWR=1;\r\n',100],
['AT+CGNSIPR=115200;\r\n',100],
['AT+CGNSTST=1;\r\n',100],
['AT+CGNSINF;\r\n',500]]

for cmd in CMD:
    sending_cmd_to_gps(cmd)


while 1:
    fd = port.read(200)        # Read the GPS data from UART
    time.sleep(.5)
    if b'$GNRMC' in fd:        # To Extract Lattitude and
        ps=fd.find(b'$GNRMC')        # Longitude
        dif=len(fd)-ps
        if dif > 50:
            data=fd[ps:(ps+50)]
            print(data)
            ds=data.find(b'A')        # Check GPS is valid
            if ds > 0 and ds < 20:
                p=list(find(data, ","))
                lat=data[(p[2]+1):p[3]]
                lon=data[(p[4]+1):p[5]]

                # GPS data calculation
                s1 = int(lat[0:2]) + Decimal(lat[2:])/60

                s2 = int(lon[0:3]) + Decimal(lon[3:])/60

                print("{0} , {1}".format(s1,s2))
