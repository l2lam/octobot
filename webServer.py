import socket
import network
import time
from machine import Timer

# Make sure the index.html file has been uploaded to the board; or you can choose to generate the html on the fly
# Original instructions here: https://www.tomshardware.com/how-to/raspberry-pi-pico-w-web-server
# and here: https://how2electronics.com/raspberry-pi-pico-w-web-server-tutorial-with-micropython/
page = open("index.html", "r")
html = page.read()
print(html);
page.close()

# Wifi config
SSID = ""
WIFI_PW = ""

# Connect to the wifi and Start the web server
def startWeb():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, WIFI_PW)
    
    # Wait for connect or fail
    wait = 10
    while wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        wait -= 1
        print('waiting for connection...')
        time.sleep(1)
     
    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('wifi connection failed')
    else:
        print('connected')
        ip=wlan.ifconfig()[0]
        print('IP: ', ip)
    
    try:
        if ip is not None:
            connection=open_socket(ip)
            serve(connection)
    except KeyboardInterrupt:
        machine.reset()

# Runs the web server, waiting for requests on port 80        
def serve(connection):
    global s
    global degree
    while True:
        print('waiting for requests')
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        
        print(request)
        if request == '/led1':
            pass
#             b1()
        elif request == '/led2':
            pass
#             b2()
        elif request == '/servoUp':
            pass
#             degree += 5
#             s.gotoDegrees(degree)
        elif request == '/servoDown':
            pass
#             degree -= 5
#             s.gotoDegrees(degree)
        
        client.send(html)
        client.close()

# The underlying socket communication for the web server
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return(connection)
