# This work is licensed under the MIT license.
# Copyright (c) 2013-2023 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# UART Control
#
# This example shows how to use the serial port on your OpenMV Cam. Attach pin
# P4 to the serial input of a serial LCD screen to see "Hello World!" printed
# on the serial LCD display.

import time
from pyb import UART
from machine import Pin

# Always pass UART 3 for the UART number for your OpenMV Cam.
# The second argument is the UART baud rate. For a more advanced UART control
# example see the BLE-Shield driver.
uart = UART(3, 19200, timeout_char=200)

pin12 = Pin("P12", Pin.IN)
#pin13 = Pin("P13", Pin.)


while True:
    uart.write("Hello World!\r")  # note: \r: ascii carriage return, \n: ascii line feed
    time.sleep_ms(1000)
