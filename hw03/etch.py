#!/usr/bin/python3
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2
import smbus
import time 


bus = smbus.SMBus(2)
matrix = 0x70
#x and y vectors will be relative to the LED matrix position divided by 2
x=3
y=3
last_position = 0
bus.write_byte_data(matrix,0x21,0)
bus.write_byte_data(matrix, 0x81,0)
bus.write_byte_data(matrix, 0xe7,0)

LEDs = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]

encode = RotaryEncoder(eQEP2)
encode.setAbsolute()
encode.enable()
encode.zero()



bus.write_i2c_block_data(matrix, 0 , LEDs)

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
    print(str(y))
    LEDs[x*2] = valueToChange
    
while 1:
    
    for k in range(8):
        y = k
        updateMatrix()
        bus.write_i2c_block_data(matrix, 0, LEDs)
       # for i in range(15):
        #    print(bin(LEDs[i]))
        time.sleep(2)
    x= x+1
