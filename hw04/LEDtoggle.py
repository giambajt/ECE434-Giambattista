#!/usr/bin/python3

from mmap import mmap
import time, struct

GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
USR3 = 1<<24
USR0 = 1<<21

with open("/dev/mem", "r+b") as f:
    mem = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)
    
packed_reg = mem[GPIO_OE:GPIO_OE+4]
reg_status = struct.unpack("<L", packed_reg)[0]
reg_status &= ~(USR3)
reg_status &= ~(USR0)
mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)

try:
    while(True):
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", USR3)
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", USR0)
        time.sleep(0.5)
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", USR3)
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", USR0)
        time.sleep(0.5)

except KeyboardInterrupt:
    mem.close()
