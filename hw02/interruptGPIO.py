#!/usr/bin/python3
import Adafruit_BBIO.GPIO as GPIO
import time as time
button = "P9_19"
button2 = "P9_21"
button3 = "P9_23"
button4 = "P9_22"
LED = "P9_11"
LED2 ="P9_13"
LED3 = "P9_15"
LED4 = "P9_17"
toggle = 0
toggle2 = 0
toggle3 = 0
toggle4 = 0
#3rd button because its the only one I can get to work
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN,pull_up_down =  GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#3rd LED
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
def turn_LED_ON(pin):
    global toggle
    if toggle == 0:
        GPIO.output(LED, GPIO.HIGH)
        toggle=1
    else:
        GPIO.output(LED, GPIO.LOW)
        toggle=0

def turn_LED_ON2(pin):
    global toggle2
    if toggle2 == 0:
        GPIO.output(LED2, GPIO.HIGH)
        toggle2=1
    else:
        GPIO.output(LED2, GPIO.LOW)
        toggle2=0

def turn_LED_ON3(pin):
    global toggle3
    if toggle3 == 0:
        GPIO.output(LED3, GPIO.HIGH)
        toggle3=1
    else:
        GPIO.output(LED3, GPIO.LOW)
        toggle3=0

def turn_LED_ON4(pin):
    global toggle4
    if toggle4 == 0:
        GPIO.output(LED4, GPIO.HIGH)
        toggle4=1
    else:
        GPIO.output(LED4, GPIO.LOW)
        toggle4=0



#GPIO.add_event_detect(button, GPIO.RISING, turn_LED_ON)

GPIO.add_event_detect(button, GPIO.BOTH, turn_LED_ON)
GPIO.add_event_detect(button2, GPIO.BOTH, turn_LED_ON2)
GPIO.add_event_detect(button3, GPIO.BOTH, turn_LED_ON3)
GPIO.add_event_detect(button4, GPIO.BOTH, turn_LED_ON4)

while 1:
    time.sleep(100/1000000.0)
