from machine import Pin, Timer, SoftI2C, I2C
from time import sleep_ms
import ubluetooth
from esp32 import raw_temperature

# Real sensor.
from hmc5883l import HMC5883L

# Fake sensor.
from qmc5883 import QMC5883


class BLE():
    def __init__(self, name):   
        self.name = name
        self.ble = ubluetooth.BLE()
        self.ble.active(True)

        self.led = Pin(2, Pin.OUT)
        self.timer1 = Timer(0)
        self.timer2 = Timer(1)
        
        
        self.disconnected()
        self.ble.irq(self.ble_irq)
        self.register()
        self.advertiser()
        
        # This lib is used with sensor real.
        #self.sensor = HMC5883L(scl= 22, sda= 21)
        
        # THis lib is used with fake sensor.
        self.sensor = QMC5883(I2C(0, scl = Pin(22), sda = Pin(21)))
        #self.sensor.set_range(0)
        #QMC5883.set_oversampling(0)
        
        # Flags Connection
        self.isConnect = False
    def connected(self):        
        self.timer1.deinit()
        self.timer2.deinit()
        
    def readSensor(self):
        x, y, z, temp = self.sensor.read_raw()
        print(f"x: {x} Y: {y} Z: {z} Temp {temp}\n")
        
        return x, y, z, t
        
    def disconnected(self):        
        self.timer1.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: self.led(1))
        sleep_ms(90)
        self.timer2.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: self.led(0))   

    def ble_irq(self, event, data):
        if event == 1:
            '''Central disconnected'''
            self.connected()
            conn_handle, addr_type, addr = data
            #print("Data recibed:", conn_handle, addr_type, addr, "\n")
            print("Conectado!\n")
            #ble.sendData("HOla from ESP32")
            self.led(1)
            
            self.isConnect = True
        
        elif event == 2:
            '''Central disconnected'''
            self.advertiser()
            self.disconnected()
            print("Desconectado!\n")
            self.isConnect = False
            
        elif event == 5:
            addr_type, addr, adv_type, rssi, adv_data = data
            print("Data recibed:", addr_type, addr, adv_type, rssi, adv_data, "\n")
            
        elif event == 3:
            
            #sleep_ms(2000)    
            '''New message received'''            
            buffer = self.ble.gatts_read(self.rx)
            message = buffer.decode('UTF-8').strip()
            print(message)
            ble.sendData("HOla from ESP32")
            
    def register(self):        
        # Nordic UART Service (NUS)
        
        NUS_UUID = '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'
        RX_UUID = '6E400002-B5A3-F393-E0A9-E50E24DCCA9E'
        TX_UUID = '6E400003-B5A3-F393-E0A9-E50E24DCCA9E'
        
        BLE_NUS = ubluetooth.UUID(NUS_UUID)
        BLE_RX = (ubluetooth.UUID(RX_UUID), ubluetooth.FLAG_WRITE | ubluetooth.FLAG_READ)
        BLE_TX = (ubluetooth.UUID(TX_UUID), ubluetooth.FLAG_NOTIFY | ubluetooth.FLAG_READ)
            
        BLE_UART = (BLE_NUS, (BLE_TX, BLE_RX,))
        SERVICES = (BLE_UART, )
        ((self.tx, self.rx,), ) = self.ble.gatts_register_services(SERVICES)
    # Service write.
    def sendData(self,data):
        print("[ESP32] send data to app..\n")
        self.ble.gatts_write(self.tx, data + '\n')
        
    # Service notify.    
    def sendNotify(self, data):
        print("[ESP32] send notify to app..\n")
        self.ble.gatts_notify(0, self.tx, data + '\n')

    def advertiser(self):
        name = bytes(self.name, 'UTF-8')
        self.ble.gap_advertise(100, bytearray('\x02\x01\x02') + bytearray((len(name) + 1, 0x09)) + name, connectable=True)
        
    def run(self):
        while True:
            if(self.isConnect):
                x, y, z, t = self.readSensor()
                self.sendData("{'x': {x}, 'y': {y}, 'z': {z}}")
                sleep_ms(5)
            else:
                pass
                
                

# test
red_led = Pin(2, Pin.OUT)
ble = BLE("ESP32-pipe")


    

