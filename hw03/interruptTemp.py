#!/usr/bin/python3

import smbus
import Adafruit_BBIO.GPIO as GPIO
import time as time

gpio = "P9_15"
tmp = smbus.SMBus(2)

addr = 0x49
tmp.write_word_data(addr, 2, 0x19)

tmp.write_word_data(addr, 3, 0x11)
tmp.write_word_data(addr, 1, 0x82)

GPIO.setup(gpio, GPIO.IN)

def readTemp(pin):
    output = tmp.read_byte_data(addr, 0)
    print(str((output*1.8) +32))

GPIO.add_event_detect(gpio, GPIO.BOTH, readTemp)

while 1:
    time.sleep(100/1000000.0)

