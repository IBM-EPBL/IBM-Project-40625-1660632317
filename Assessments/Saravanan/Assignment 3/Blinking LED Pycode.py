# Saravanan

# Python code for blinking LED

import machine
import utime

led _ red = machine. Pin(15, machine.Pin.OUT)
led_yeltow = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine. Pin. OUT)

white True:
    led_red.value(1)
    utime.sleep(5)
    led_yellow.value(1)
    utime.sleep(2)
    led red.value(0)
    led_yellow.value(0)
    led_green.value(1)
    utime.sleep(5)
    led_green.value(0)
    led_yellow.value(l)
    utime.sleep(5)
    led_yellow.value(O)
