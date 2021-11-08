#!/usr/bin/python3

with open('/sys/class/hwmon/hwmon0/temp1_input') as f:
    lines = f.readlines()
f.close()
print(lines[0])
with open('/sys/class/hwmon/hwmon1/temp1_input') as f:
    lines = f.readlines()
f.close()
print(lines[0])
with open('/sys/class/hwmon/hwmon2/temp1_input') as f:
    lines = f.readlines()
f.close()
print(lines[0])
