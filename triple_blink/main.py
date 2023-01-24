from machine import Pin
import time

green_led = Pin(0, Pin.OUT)
yellow_led = Pin(4, Pin.OUT)
red_led = Pin(5, Pin.OUT)
red_br_led = Pin(2, Pin.OUT)

s = 0.05

while True:
    green_led.on()
    yellow_led.off()
    red_led.off()
    red_br_led.off()
    time.sleep(s)
    
    green_led.off()
    yellow_led.on()
    red_led.off()
    red_br_led.off()
    time.sleep(s)
    
    green_led.off()
    yellow_led.off()
    red_led.on()
    red_br_led.off()
    time.sleep(s)
    
    green_led.off()
    yellow_led.off()
    red_led.off()
    red_br_led.on()
    time.sleep(s)
    
    