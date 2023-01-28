#Librerias
import time
from machine import Pin
import network
import socket

#Configuración inicial de WiFi
ssid = 'Thunderbluff'  #Nombre de la Red
password = '9094popa' #Contraseña de la red
wlan = network.WLAN(network.STA_IF)

wlan.active(True) #Activa el Wifi
wlan.connect(ssid, password) #Hace la conexión

while wlan.isconnected() == False: #Espera a que se conecte a la red
    pass

print('Conexion con el WiFi %s establecida' % ssid)
print(wlan.ifconfig()) #Muestra la IP y otros datos del Wi-Fi

#Salidas
cafetera = Pin(2, Pin.OUT)
# cocina = Pin(4, Pin.OUT)

#Pagina web
def web_page():  
    html = """    <html>

            <head>
                <title>MicroTutoriales DC</title>
                <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
            </head>
            
            <body>
                <!-- Image and text -->            
                <div class="container">
                    <div class="row">
                        <div class="col-sm-12 col-md-4">
                            <div class="card" style="width: 18rem;">
                                
                                    <h5 class="card-title">LED 1</h5>
                                    <br>
                                    <a href="/cafetera=on" class="btn btn-success">ON</a>
                                    <a href="/cafetera=off" class="btn btn-danger">OFF</a>
                                
                            </div>
                        </div>
                        <div class="col-sm-12 col-md-4">
                            <div class="card" style="width: 18rem;">
                                    <h5 class="card-title">LED 2</h5>
                                    <br>
                                    <a href="/cocina=on" class="btn btn-success">ON</a>
                                    <a href="/cocina=off" class="btn btn-danger">OFF</a>
                            </div>
                        </div>
                    </div>
                </div>
            </body>
            
            </html>  """
    return html

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(('', 80))
tcp_socket.listen(3)

while True:
    conn, addr = tcp_socket.accept()
    print('Nueva conexion desde:  %s' % str(addr))
    request = conn.recv(1024)
    print('Solicitud = %s' % str(request))
    request = str(request)
    if request.find('/cafetera=on') == 6:
        print('Cafetera ON')
        cafetera.value(1)
    if request.find('/cafetera=off') == 6:
        print('Cafetera OFF')
        cafetera.value(0)
    # if request.find('/cocina=on') == 6:
    #     print('Cafetera ON')
    #     cocina.value(1)
    # if request.find('/cocina=off') == 6:
    #     print('Cafetera OFF')
    #     cocina.value(0)

    # Mostrar Página
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
