#!/bin/sh


echo tmp101 0x4a > /sys/class/i2c-adapter/i2c-1/new_device

temp=$(cat /sys/class/i2c-adapter/i2c-1/1-004a/hwmon/hwmon0/temp1_input)
temp2=$(($temp /1000))
temp3=$(($temp2 *9))
temp4=$(($temp3 /5))
temp5=$(($temp4 +32))
echo $temp5
