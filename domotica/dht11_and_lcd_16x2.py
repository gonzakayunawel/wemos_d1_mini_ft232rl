# Importar librerías
from machine import I2C, ADC, Pin
import time
import dht
# Para ejecutar esta línea se debe tener dentro de la placa Wemos D1 Mini (esp8266)
# las siguientes librerías:
# - circuitpython_i2c_lcd.py
# - esp8266_i2c_lcd.py
# - lcd_api.py
from esp8266_i2c_lcd import I2cLcd

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400_000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.backlight_on()

# Crear objeto sensor con la librería
# y el sensor correspondiente
sensor = dht.DHT11(Pin(16))

while True:
    # activar la medición del sensor
    sensor.measure()
    # imprimir los valores de medición
    t = sensor.temperature()
    rh = sensor.humidity()
    print(f'Temp: {t} Celsius, RH: {rh} %')
    #imprimir por LCD 16x2
    lcd.putstr(f'Temp: {t} Celsius, RH: {rh} %')
    time.sleep(2)
    lcd.clear()
     
    

