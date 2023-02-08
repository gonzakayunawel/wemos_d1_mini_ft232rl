# Importar librerías
from machine import I2C, ADC, Pin
import time
from esp8266_i2c_lcd import I2cLcd

i2x = I2C(scl=Pin(5), sda=Pin(4), freq=400_000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.backlight_on()
lcd.clear()

lcd.putstr('Hello Word!')

# Valor de voltaje del pin análogo ADC A0
# analog_value = ADC(0)
# 
# # Factor de conversión para pasar de valor analógico a digital
# conversion_factor = 3.3 / 1024
# 
# while True:
#     # valor de voltaje de señal del sensor lm35dz
#     sensor_signal_value = analog_value.read()
#     # voltaje análogo a digital
#     convert_voltaje = sensor_signal_value * conversion_factor
#     # temperatura en Celsius
#     tempC = round(convert_voltaje/ (10/1000), 1)
#      
#     print(f'Temperature {tempC} °C')
#      
#     time.sleep(2)

