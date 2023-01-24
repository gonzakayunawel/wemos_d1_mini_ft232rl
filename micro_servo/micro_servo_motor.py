from machine import Pin, PWM
import time
# Wemos D1 mini with chip FT232RL(FTDI)

# pin 13 = D7
servo1 = PWM(Pin(13))

# freq: 50hz = 20 ms
servo1.freq(50)

# grades ang
grade_0 = 500_000
grade_90 = 1_500_000
grade_180 = 2_500_000

# pin 5 = D1
# pin 4 = D2
led_yellow = Pin(5, Pin.OUT)
led_green = Pin(4, Pin.OUT)

# time seconds
time_s = 0.5

while True:
    servo.duty_ns(grade_0)
    led_yellow.on()
    led_green.off()
    time.sleep(time_s)
    servo.duty_ns(grade_90)
    led_yellow.off()
    led_green.on()
    time.sleep(time_s)