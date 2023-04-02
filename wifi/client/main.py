# https://www.infineon.com/cms/jp/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-4-802.11n/cyw43439/

import network
import utime
import socket
import machine

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

def http_get(host, port):
    ai = socket.getaddrinfo(host, port)
    addr = ai[0][-1]

    # Create a socket and make a HTTP request
    s = socket.socket()
    s.connect(addr)
    s.send(b"GET / HTTP/1.0\r\n\r\n")

    # Print the response
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break


host = "192.168.0.1"
port = 80
try:
    ip = connect(ssid, pw)
    http_get(host, port)
except KeyboardInterrupt:
    machine.reset()
