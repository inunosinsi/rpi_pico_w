import network
import utime
import machine
import urequests

# ssidは必ず2.4GHz帯の方
ssid = "your ssid"
pw = "password"

# POST先のURL
url = "http://192.168.0.1:80"

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
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def http_post(url, value):
    # https://docs.openmv.io/library/urequests.html
    body = "value=%s" % (value)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = urequests.post(url, data=body, headers=headers)
    print(response)

try:
    ip = connect(ssid, pw)
    http_post(url, "1")
except KeyboardInterrupt:
    machine.reset()
