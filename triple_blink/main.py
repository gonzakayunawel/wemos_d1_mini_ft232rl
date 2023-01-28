from machine import Pin
import time

green_led = Pin(2, Pin.OUT)
yellow_led = Pin(0, Pin.OUT)
yellow_2_led = Pin(4, Pin.OUT)


s = 0.05

while True:
    green_led.on()
    yellow_led.off()
    yellow_2_led.off()
    time.sleep(s)
    
    green_led.off()
    yellow_led.on()
    yellow_2_led.off()
    time.sleep(s)
    
    green_led.off()
    yellow_led.off()
    yellow_2_led.on()
    time.sleep(s)
    
    