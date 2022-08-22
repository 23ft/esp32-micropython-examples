
global station, Pin, lamp1, lamp2, led_user, gc

from modules.mqtt_as import MQTTClient, config
import uasyncio as asyncio


"""
    23ft - 7 agosto - 2022

    * La esp32 no tiene tanto alcanze de wifi o en la zona donde estoy esta muy distante o con muchos obstaculos.
    importante tener una buena latencia para no tener perdida de datos, la libreria MQTT de peterhinch gestiona
    las desconexiones y ayuda a solucionar una parte esta problematica.
    
    * Se espera probar sockets directamente para validar si el fallo era de la ESP32 o de mi ubicacion al router.
    
    23ft - 22 agosto - 2022
    
    * se logra formatear codigo a version batuizada 2. Se integra nuevos topics de subscricion donde se lograra informar hacerca del estado de los
    elementos controlados por el LIGHST-MANAGER-ESP32.
    
    * pendiente estudiar bien asyncio para dar una mejora futura en ese aspecto, por ahora se comprueba un funcionamiento correcto.
    
"""


SERVER = '198.58.99.52'  # Change to suit e.g. 'iot.eclipse.org'
TOPIC = ['house-spring/lamp', 'request-status/lamps', 'request-status/lamps/response']

# flags and counters.
outages = 0
flag_enabled = None

def callback(topic, msg, retained):
    print((topic, msg, retained))
    
    if topic.decode() == TOPIC[0]:
        if msg.decode() == 'state=lamp1/on':
            lamp1.value(1)
        if msg.decode() == 'state=lamp1/off':
            lamp1.value(0)
        
        if msg.decode() == 'state=lamp2/on':
            lamp2.value(1)
        if msg.decode() == 'state=lamp2/off':
            lamp2.value(0)
    elif topic.decode() == TOPIC[1]:
       print("[async-callback-mqtt] Recived sms from topic: ", topic.decode())     
async def wifi_han(state):
    global outages
    #blue_led  # Light LED when WiFi down
    if state:
        pass
        print('[async-wifi-han] We are connected to broker.')
    else:
        outages += 1
        print('[async-wifi-han] WiFi or broker is down.')
    await asyncio.sleep(1)

async def conn_han(client):
    global flag_enabled
    for top in TOPIC:
        print("[async-conn-han] Subscribe ESP32 to: ", top)
        await client.subscribe(top, 1)
        await asyncio.sleep_ms(100)
    await asyncio.sleep_ms(100)
    flag_enabled = True

async def main(client):
    global flag_enabled
    n = 0
    
    await client.connect()    
    print("[async-main] Waiting subscritions...")
    while True:
        
        #print("[async-main] flag_enabled: ", flag_enabled)
        while flag_enabled:
            led_user.value(not led_user.value())
            if n == 20:
                gc.collect()
                print("[async-main] publish check for broker...")
                print("[async-main] broker_up result is: ", await client.broker_up())
                await client.publish(b'house-spring/lamp1', b'\n Saludos ESP32 #{}'.format(n))
                n = 0

            print('[async-main] count', n)
            # If WiFi is down the following will pause for the duration.

            n += 1
            await asyncio.sleep_ms(500)
        await asyncio.sleep_ms(200)
config['ssid'] = 'Sebas y felipe'
config['wifi_pw'] = 'Manuelpipe1'
config['subs_cb'] = callback        # Callback for sms recibeds.
config['connect_coro'] = conn_han   # Hanlder to connect to topics.
config['server'] = SERVER           # server broker.
config['port'] = 1883               # port broker.
config['keepalive'] = 120           
config['wifi_coro'] = wifi_han      # hanlder wifi cheing.
config['will'] = (TOPIC[0], 'Goodbye cruel world!', False, 0)

#MQTTClient.DEBUG = False  # Optional: print diagnostic messages
client = MQTTClient(config)
client.DEBUG = False

try:
    asyncio.run(main(client))   # ejecutar bucle de eventos asincrono.
finally:
    client.close()              # Prevent LmacRxBlk:1 errors