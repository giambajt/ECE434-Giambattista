#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time as time

pin = "P9_30"

GPIO.setup(pin, GPIO.OUT)

while 1:
    GPIO.output(pin, GPIO.HIGH)
    GPIO.output(pin, GPIO.LOW)
