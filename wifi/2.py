# document
# https://micropython-docs-ja.readthedocs.io/ja/latest/esp8266/tutorial/network_tcp.html#simple-http-server

import network
import time
import socket

# ssidは必ず2.4GHz帯の方
ssid = "your ssid"
pw = "your pw"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, pw)

wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    time.sleep(1)
    
if wlan.status() != 3:
    raise RuntimeError("network connection failed")
else:
    print("Connected")
    ifcnf = wlan.ifconfig()
    print("ip = " + ifcnf[0])
    
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
sock = socket.socket()
sock.bind(addr)
sock.listen(1)
print('listening on', addr)

while True:
    cl, addr = sock.accept()
    print('client connected from', addr)
        
    # Create and send response
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send("<!DOCTYPE><html><body>hello rpi pico w</body></html>\n")
    cl.close()
