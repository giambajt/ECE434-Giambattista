#!/usr/bin/python3
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time 
from flask import Flask, render_template, request
app = Flask(__name__)

button = "P9_13"
bus = smbus.SMBus(1)
matrix = 0x70
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

def updateLEDs():
    global matrix
    global LEDs
    updateMatrix()
    bus.write_i2c_block_data(matrix, 0, LEDs)
    time.sleep(10000/1000000.0)

updateLEDs()

@app.route("/")
def index():
    templateData = {
            'title' : 'etch-a-sketch',
            'Direction' : 'none',
    }
    return render_template('sketch.html', **templateData)
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    global x
    global y
    global bus
    global LEDs
    if deviceName == 'button':
        actuator = matrix
    if action == "left":
        x = x+1
    if action == "right":
        x = x-1
    if action == "up":
        y = y-1
    if action == "down":
        y=y+1
    if action == "clear":
        x=3
        y=4
        LEDs=[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
        bus.write_i2c_block_data(matrix, 0, LEDs)
    updateLEDs()
    templateData = {
        'Direction' : action,
    }
    return render_template('sketch.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8081, debug=True)
