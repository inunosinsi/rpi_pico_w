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
    while wlan.isconnected() == False:
        print("Waiting for connection...")
        utime.sleep(1)
    #print(wlan.ifconfig())
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def http_get(url):
    print(url)
    
        
try:
    ip = connect(ssid, pw)
    led.on()
except KeyboardInterrupt:
    machine.reset()
