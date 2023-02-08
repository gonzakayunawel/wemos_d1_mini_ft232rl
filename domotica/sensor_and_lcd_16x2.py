# Importar librerías
from machine import I2C, ADC, Pin
import time
# Para ejecutar esta línea se debe tener dentro de la placa Wemos D1 Mini (esp8266)
# las siguientes librerías:
# - circuitpython_i2c_lcd.py
# - esp8266_i2c_lcd.py
# - lcd_api.py
from esp8266_i2c_lcd import I2cLcd

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400_000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.backlight_on()
lcd.clear()

# Valor de voltaje del pin análogo ADC A0
analog_value = ADC(0)

# Factor de conversión para pasar de valor analógico a digital
conversion_factor = 3.3 / 1024

while True:
    # valor de voltaje de señal del sensor lm35dz
    sensor_signal_value = analog_value.read()
    # voltaje análogo a digital
    convert_voltaje = sensor_signal_value * conversion_factor
     
    print(f'Current Voltaje: {convert_voltaje} Volts.')
#     lcd.putstr(f'Temperature {tempC} °C')
#     lcd.clear()
     
    time.sleep(2)

