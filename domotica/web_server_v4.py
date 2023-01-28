#Módulos a utilizar
import time
from machine import Pin
import network
import socket

#Salidas
led1 = Pin(2, Pin.OUT)
led2 = Pin(0, Pin.OUT)
led3 = Pin(4, Pin.OUT)
led4 = Pin(5, Pin.OUT)

#Configuración inicial de WiFi
ssid = 'Thunderbluff'  #Nombre de la Red
password = '9094popa' #Contraseña de la red
wlan = network.WLAN(network.STA_IF)

wlan.active(True) #Activa el Wifi
wlan.connect(ssid, password) #Hace la conexión

while wlan.isconnected() == False: #Espera a que se conecte a la red
    pass

print('Conexion con el WiFi %s establecida' % ssid)
def led_turn():
    led2.on()
    time.sleep(0.3)
    led2.off()
print(wlan.ifconfig()) #Muestra la IP y otros datos del Wi-Fi
led_turn()

#Pagina web
def web_page():
    html = """<html>
<head>
<title>Test Site for Wemos 2</title>
<meta http-equiv="Content-Type" content="text/html; charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{background:#201f1f}.btn-title{font-weight:bold;color:white}.btn-danger{color:white;background:red}.btn-success{color:white;background:green}.btn{text-decoration:none;padding:10px;margin:10px;border:1px solid;border-radius:5px;box-shadow:inset 0 -4px 10px black}.button:hover{box-shadow:inset 1px 0 10px 7px #000000d1}.container{text-align:center}.button-cont{margin:40px}</style>
</head>
<body>
<div class="container">
<div class="row">
<h5 class="btn-title">LED 1</h5>
<a href="/led1=on" class="btn btn-success">ON</a>
<a href="/led1=off" class="btn btn-danger">OFF</a>
</div>
</div>
<div class="container">
<div class="row">
<h5 class="btn-title">LED 2</h5>
<a href="/led2=on" class="btn btn-success">ON</a>
<a href="/led2=off" class="btn btn-danger">OFF</a>
</div>
</div>
<div class="container">
<div class="row">
<h5 class="btn-title">LED 3</h5>
<a href="/led3=on" class="btn btn-success">ON</a>
<a href="/led3=off" class="btn btn-danger">OFF</a>
</div>
</div>
<div class="container">
<div class="row">
<h5 class="btn-title">LED 4</h5>
<a href="/led4=on" class="btn btn-success">ON</a>
<a href="/led4=off" class="btn btn-danger">OFF</a>
</div>
</div>
<div class="container">
<div class="row">
<h5 class="btn-title">Secuencia de LEDs</h5>
<a href="/led5=on" class="btn btn-success">ON</a>
<a href="/led5=off" class="btn btn-danger">OFF</a>
</div>
</div>
</body>
</html>"""    
    return html

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(('', 80))
tcp_socket.listen(5)

def triple_blink(s=0.5):
    on = 0
    while on<5:
        led1.on()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(s)
        on += 1
        
        led1.off()
        led2.on()
        led3.off()
        led4.off()
        time.sleep(s)
        on += 1
        
        led1.off()
        led2.off()
        led3.on()
        led4.off()
        time.sleep(s)
        on += 1
        
        led1.off()
        led2.off()
        led3.off()
        led4.on()
        time.sleep(s)
        on += 1
        
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(s)
        on += 1


while True:
    conn, addr = tcp_socket.accept()
    print('Nueva conexion desde:  %s' % str(addr))
    request = conn.recv(1024)
    print('Solicitud = %s' % str(request))
    request = str(request)
    print(request)
    
    if request.find('/led1=on') == 6:
        print('Led 1 ON')
        led1.value(1)
    if request.find('/led1=off') == 6:
        print('Led 1 OFF')
        led1.value(0)
    
    if request.find('/led2=on') == 6:
        print('Led 2 ON')
        led2.value(1)
    if request.find('/led2=off') == 6:
        print('Led 2 OFF')
        led2.value(0)
        
    if request.find('/led3=on') == 6:
        print('Led 3 ON')
        led3.value(1)
    if request.find('/led3=off') == 6:
        print('Led 3 OFF')
        led3.value(0)
        
    if request.find('/led4=on') == 6:
        print('Led 4 ON')
        led4.value(1)
    if request.find('/led4=off') == 6:
        print('Led 4 OFF')
        led4.value(0)
        
    if request.find('/led5=on') == 6:
        print('Secuencia ON 0.2 seg.')
        triple_blink(0.2)
    if request.find('/led5=off') == 6:
        print('All LEDs OFF')
        led1.off()
        led2.off()
        led3.off()
        led4.off()

    # Mostrar Página
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
    
    
    
