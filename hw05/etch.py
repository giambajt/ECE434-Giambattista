#!/usr/bin/python3
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2,eQEP0
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time 

button = "P9_13"
bus = smbus.SMBus(1)
matrix = 0x70
accel = 0x53
lastxAccl = 0
lastyAccl = 0
#x and y vectors will be relative to the LED matrix position divided by 2
x=3
y=4
last_position_x = 0
last_position_y = 0
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
bus.write_byte_data(matrix,0x21,0)
bus.write_byte_data(matrix, 0x81,0)
bus.write_byte_data(matrix, 0xe7,0)

LEDs = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]


bus.write_i2c_block_data(matrix, 0 , LEDs)
bus.write_byte_data(accel, 0x2C, 0x0A)
bus.write_byte_data(accel, 0x2D, 0x08)
bus.write_byte_data(accel, 0x31, 0x08)

def resetMatrix(pin):
    global x
    global y
    global matrix
    global LEDs
    global bus
    LEDs = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    x = 3
    y = 4
    bus.write_i2c_block_data(matrix, 0, LEDs)



def defineY(param):
    if param == 0:
        return 1
    elif param ==1:
        return 2
    elif param == 2:
        return 4
    elif param == 3:
        return 8
    elif param == 4:
        return 16
    elif param == 5:
        return 32
    elif param == 6:
        return 64
    elif param == 7:
        return 128
# make sure that x and y cannot go above 7 or below 0
def updateMatrix():
    global x
    global y
    global LEDs
    matrixY = defineY(y)
    valueToChange = LEDs[x*2]
    valueToChange = valueToChange | matrixY
    LEDs[x*2] = valueToChange
    for i in range(8):
        LEDs[i*2+1] = 0
    redValueToChange = LEDs[x*2+1]
    redValueToChange = redValueToChange | matrixY
    LEDs[x*2+1] = redValueToChange
    
GPIO.add_event_detect(button, GPIO.BOTH, resetMatrix)

while 1:
    
    data0 = bus.read_byte_data(accel, 0x32)
    data1 = bus.read_byte_data(accel, 0x33)
    xAccl = ((data1&0x03) * 256) + data0
    if xAccl > 511:
        xAccl -= 1024
    data2 = bus.read_byte_data(accel, 0x34)
    data3 = bus.read_byte_data(accel, 0x35)
    yAccl = ((data3&0x03) * 256) + data2
    if yAccl > 511:
        yAccl -= 1024
    if lastxAccl < (xAccl-30):
        x = x-1
        if x < 0:
            x = 0
    elif lastxAccl > (xAccl+30):
        x = x+1
        if x > 7:
            x=7
    elif lastyAccl < (yAccl-30):
        y = y-1
        if y<0:
            y=0
    elif lastyAccl > (yAccl+30):
        y = y+1
        if y>7:
            y=7
    
    lastyAccl = yAccl
    lastxAccl = xAccl


    updateMatrix()
    bus.write_i2c_block_data(matrix, 0, LEDs)
    time.sleep(100000/1000000.0)
