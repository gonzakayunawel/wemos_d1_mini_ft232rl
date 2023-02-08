# Importar librerías
from machine import Pin
import time
import dht

# Crear objeto sensor con la librería
# y el sensor correspondiente
sensor = dht.DHT11(Pin(16))

while True:
    # activar la medición del sensor
    sensor.measure()
    # imprimir los valores de medición
    t = sensor.temperature()
    rh = sensor.humidity()
    
    print(f'Temp: {t} °C, RH: {rh} %')
     
    time.sleep(2)
