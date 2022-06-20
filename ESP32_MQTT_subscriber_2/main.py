"""
# Connect the ESP32 to broker MQTT usign micropython v1.16.
# ---------------------------------------------------------
# Using the protocol MQTT for IoT, in this case de ESP32 function how pub and sub.
# The server/broker local is a pc with mosquitto, is a MQTT broker open-source.
# ---------
# 23ft
# July 2021.
# ---------
"""

"""
** Documentacion **

* MQTTOBJ = MQTT.MQTTClient(mqtt_id, mqtt_host, mqtt_port) --> Creamos cliente para manejo MQTT, clase MQTTClient()
* MQTTOBJ.connect() --> Conectamos el cliente al broker MQTT.
* MQTTOBJ.set_callback(function) --> Recibe la funcion que tomara los mensajes nuevos de las subs.
* MQTTOBJ.check_msg() --> Revisa si hay nuevos mensajes, posteriomente se los pasa a la funcion Callback definida.
* MQTTOBJ.subscribe(topic) --> Suscribir el cliente a el tema que se le pase.
* MQTTOBJ.disconnect() --> Desconecta al cliente del broker MQTT


"""

import MQTT

"""
***Global variabels***
"""
global mqtt_id, mqtt_host, mqtt_port, mqtt_user, mqtt_pass, led_esp
mqtt_stop_esp = False

"""
***Functions***
"""
# Callback function to new messages in subs.
def sub_sms(topic, payload):
    led_esp.value(1)
    global mqtt_stop_esp
    print("[ESP32 - Callback] topic: ", topic, "\n [ESP32 - Callback] payload: ", payload)
    
    if payload == b'END':
        print('end mensaje')
        mqtt_stop_esp = True
    led_esp.value(0)
        
# Function to subscribe the ESP32 at topics in broker.
def subs (client, topics=[]):
    for t in topics:
        print('[Function Subs] Subscribe to topic: ', t)
        client.subscribe(t)

"""
*** Main program ***
"""

# conexion MQTT
client = MQTT.MQTTClient(mqtt_id, mqtt_host, mqtt_port)
client.set_callback(sub_sms)
client.connect()
subs(client, [b'home', b'home/led=secuencia1'])

# Loop for subscibtions an recive new messages.
while True:
    client.check_msg()

    if mqtt_stop_esp:
        print('\n\n\n[ESP32 logs] The publish payload in the server is END, close de connection')
        mqtt_stop_esp = False
        client.disconnect()
        break
        
            
    