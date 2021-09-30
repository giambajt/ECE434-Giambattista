GPIO via mmap:
LEDToggle.py toggles USR3 and USR0 LEDs using mmap calls.  No setup is required for this

ToggleLEDfast.py toggles P8_15 as fast as possible and I measured it to be around 90kHz.

KernelI2C.sh will read from the tmp101 sensor.  The setup script is required to setup the
config pins for I2C.  It works on I2C 1 bus and there is a commented out line in setup.sh 
that will add the tmp101 device to the kernel if it hasn't already been added.  The address
may need to be changed

etch.py runs etch-a-sketch on the LED matrix from a flask server.  Each time a button is
clicked on the web browser the matrix moves over one square in the direction that was clicked.
There is also a clear button.  This also requires the I2C so setup.sh will need to be run if it
hasn't been already.  

For the LCD i have text.sh that will automatically put text on the LCD screen and there are 
images in the directory for someone to manually put them on the LCD using the shell command
sudo fbi -noverbose -T 1 -a boris.png


