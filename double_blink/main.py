from machine import Pin
import time

led_yellow = Pin(5, Pin.OUT)
led_green = Pin(4, Pin.OUT)
time_s = 0.5
while True:
    led_yellow.on()
    led_green.off()
    time.sleep(time_s)
    led_yellow.off()
    led_green.on()
    time.sleep(time_s)