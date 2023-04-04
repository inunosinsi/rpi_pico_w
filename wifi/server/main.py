# sample code
# https://projects.raspberrypi.org/en/projects/get-started-pico-w/2
# document
# https://micropython-docs-ja.readthedocs.io/ja/latest/esp8266/tutorial/network_tcp.html#simple-http-server

import network
import utime
import socket
import machine


led = machine.Pin("LED", machine.Pin.OUT)
led.off()

# ssidは必ず2.4GHz帯の方
ssid = "your ssid"
pw = "your password"

# Connect to WLAN
def connect(ssid, pw):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, pw)
    wait = 0
    while wlan.isconnected() == False:
        print("Waiting for connection...")
        utime.sleep(1)
        wait += 1
        if wait > 20:
            raise RuntimeError("network connection failed")
    #print(wlan.ifconfig())
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

# Open a socket
def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

# Build html
def build_html():
    return f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>raspberry pi pico w</title>
            </head>
            <body>
            hello raspberry pi pico w!
            </body>
            </html>
            """

# Start a web server
def serve(connection):
    while True:
        client = connection.accept()[0]
        data = client.recv(1024)
        if data:
            print(str(data, 'utf8'), end='')
        client.send(build_html())
        client.close()
        
try:
    ip = connect(ssid, pw)
    led.on()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
