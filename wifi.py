import network
import time

def do_connect(essid,passwd):  
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(essid, passwd)
        while not wlan.isconnected():
            time.sleep_ms(1000)
            print("connect again")
    print('network config:', wlan.ifconfig())