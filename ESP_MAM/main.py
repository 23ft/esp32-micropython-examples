import network

ssid = 'Sebas y felipe'

conn = network.WLAN(network.STA_IF)
conn.active(True)
conn.connect(ssid, 'Manuelpipe1')

while not conn.isconnected():
    pass

print("Connected! to {red}".format(red=ssid))




    
    

