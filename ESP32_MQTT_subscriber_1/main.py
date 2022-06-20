global topic_r,  msg_r, cont, espid, stop, led
subr = False
stop = False
led = False

def sub_cb(topic, msg):
    global subr, stop, led
    
    print("[Callback Function | MQTT - Check] => ", (topic, msg))
    subr = True
    
    # Mensaje de parada loop en ESP32.
    if msg == b'END':
        stop = True
    
    # Mensaje prender led.
    if msg == b'LED2=ON':
        led = True
    elif msg == b'LED2=OFF':
        led = False
    


"""
Variables principales de la conexion MQTT
"""
clientId = espid
mqttbroker = "ioticos.org"
mqttport = 1883
user = "kxkNYIPpTKyCtW0"
password = "tERnRpj5b5BC91N"

# topico a publicar.
topic_sub = b'mmkHaipZIjJhWce'
topic_pub = b'mmkHaipZIjJhWce/respuesta'

"""
Conexion MQTT.
"""
# Creamos cliente de conexion para servidor[broker] MQTT.
client = MQTTClient(clientId, mqttbroker, mqttport, user, password)

client.set_callback(sub_cb)

# conectamos cliente por el metodo connect().
client.connect()

client.subscribe(topic_sub)

"""
# mandamos una publicacion al topico_pub, con el mensaje del parametro siguiente.
client.publish(topic_pub, b'[ESP32 - 1] Mensaje desde ESP32')
"""

led_esp = Pin(2, Pin.OUT)

while True:
    
    try:
        client.check_msg()
        
        # Peticion de prender led.
        if led:
            led_esp.value(1)
        else:
            led_esp.value(0)
        
        # Peteicion de detener loop.
        if stop:
            break
        
        # Mensaje respusta al recibir por subr.
        if subr:
            msg = b"[MQTT - ESP32] Mensaje recibido!."
            client.publish(topic_pub, msg)
            subr = False
            print("[MQTT - Publish] Respuesta hecha al broker.")
            
        time.sleep(1)
    except:
        print("[MQTT - subscribe] Error in loop to check new mesages!")


