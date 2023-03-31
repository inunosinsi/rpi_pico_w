import network
import time

ssid = "your ssid" # 2.4GHzの方を指定
pw = "your password"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, pw)

# 接続確認
# ステータスコード → https://micropython-docs-ja.readthedocs.io/ja/latest/library/network.WLAN.html#network.WLAN.status
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
