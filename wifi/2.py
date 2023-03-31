
import network
import time
import socket

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
    cnf = wlan.ifconfig()
    print("ip = " + cnf[0])
    
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
sock = socket.socket()
sock.bind(addr)
sock.listen(1)
print('listening on', addr)

while True:
    try: 
        conn, addr = sock.accept()
        print('client connected from', addr)
        
        # Create and send response
        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.send("<!DOCTYPE><html><body>hello rpi pico w</body></html>")
        conn.close()
        
    except OSError as e:
        conn.close()
        print('connection closed')
