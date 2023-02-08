# Importar librerías
from machine import ADC, Pin
import time

# Valor de voltaje del pin análogo ADC A0
analog_value = ADC(0)

# Factor de conversión para pasar de valor analógico a digital
conversion_factor = 3.3 / 1024

while True:
    # valor de voltaje de señal del sensor lm35dz
    sensor_signal_value = analog_value.read()
    # voltaje análogo a digital
    convert_voltaje = sensor_signal_value * conversion_factor
    # temperatura en Celsius
    tempC = round(convert_voltaje/ (10/1000), 1)
     
    print(f'Temperature {tempC} °C')
     
    time.sleep(2)
