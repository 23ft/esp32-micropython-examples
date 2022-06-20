

# SPI CMD

READ_CMD = 0x80

# MPU9250 registers
ACCEL_OUT = 0x3B
GYRO_OUT = 0x43
TEMP_OUT = 0x41
EXT_SENS_DATA_00 = 0x49
ACCEL_CONFIG = 0x1C
ACCEL_FS_SEL_2G = 0x00
ACCEL_FS_SEL_4G = 0x08
ACCEL_FS_SEL_8G = 0x10
ACCEL_FS_SEL_16G = 0x18
GYRO_CONFIG = 0x1B
GYRO_FS_SEL_250DPS = 0x00
GYRO_FS_SEL_500DPS = 0x08
GYRO_FS_SEL_1000DPS = 0x10
GYRO_FS_SEL_2000DPS = 0x18
ACCEL_CONFIG2 = 0x1D
DLPF_184 = 0x01
DLPF_92 = 0x02
DLPF_41 = 0x03
DLPF_20 = 0x04
DLPF_10 = 0x05
DLPF_5 = 0x06
CONFIG = 0x1A
SMPDIV = 0x19
INT_PIN_CFG = 0x37
INT_ENABLE = 0x38
INT_DISABLE = 0x00
INT_PULSE_50US = 0x00
INT_WOM_EN = 0x40
INT_RAW_RDY_EN = 0x01
PWR_MGMNT_1 = 0x6B
PWR_CYCLE = 0x20
PWR_RESET = 0x80
CLOCK_SEL_PLL = 0x01
PWR_MGMNT_2 = 0x6C
SEN_ENABLE = 0x00
DIS_GYRO = 0x07
USER_CTRL = 0x6A
I2C_MST_EN = 0x20
I2C_MST_CLK = 0x0D
I2C_MST_CTRL = 0x24
I2C_SLV0_ADDR = 0x25
I2C_SLV0_REG = 0x26
I2C_SLV0_DO = 0x63
I2C_SLV0_CTRL = 0x27
I2C_SLV0_EN = 0x80
I2C_READ_FLAG = 0x80
MOT_DETECT_CTRL = 0x69
ACCEL_INTEL_EN = 0x80
ACCEL_INTEL_MODE = 0x40
LP_ACCEL_ODR = 0x1E
WOM_THR = 0x1F
WHO_AM_I = 0x75
FIFO_EN = 0x23
FIFO_TEMP = 0x80
FIFO_GYRO = 0x70
FIFO_ACCEL = 0x08
FIFO_MAG = 0x01
FIFO_COUNT = 0x72
FIFO_READ = 0x74

# AK8963 registers
AK8963_I2C_ADDR = 0x0C
AK8963_HXL = 0x03
AK8963_CNTL1 = 0x0A
AK8963_PWR_DOWN = 0x00
AK8963_CNT_MEAS1 = 0x12
AK8963_CNT_MEAS2 = 0x16
AK8963_FUSE_ROM = 0x0F
AK8963_CNTL2 = 0x0B
AK8963_RESET = 0x01
AK8963_ASA = 0x10
AK8963_WHO_AM_I = 0x00

import re
import ubinascii
from machine import SPI, Pin
from utime import sleep_ms
"""

    binascii.hexlify(x) -> Convert the bytes in X object to a hexadecimal representation. 
    Returns a bytes object.
    
    
"""
class MPU9250():
    def __init__(self):
        # Create SPI.
        self.cs = cs = Pin(26, mode=Pin.OUT, value=1)
        self.sens = SPI(1, 400000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
        
        self.buff_r = bytearray(1)
        self.buff = None
        self.data_recv = None
        
        # enable I2C master mode
        #self.writeRegister(USER_CTRL,I2C_MST_EN)
        self.read_reg(WHO_AM_I)
        #self.write_reg(USER_CTRL, I2C_MST_EN)
        #self.write_reg(I2C_MST_CTRL, I2C_MST_CLK)
        
        #self.readAK(AK8963_WHO_AM_I)
        
     
    def mpuActive(self):
        self.cs.value(0)
    
    def mpuDisable(self):
        self.cs.value(1)
    
    def spi_write(self, data, register):
        datax = bytearray(1)
        datax[0] = register
        self.mpuActive()
        self.sens.write(datax) # send register to write.
        
        datax[0] = data
        self.sens.write(datax)     # send data to pre-select register.
        self.mpuDisable()
        
        return True

    """
    From datasheet:
    SPI read and write operations are completed in 16 or more clock cycles (two or more bytes). The
    first byte contains the SPI Address, and the following byte(s) contain(s) the SPI data. The first bit
    of the first byte contains the Read/Write bit and indicates the Read (1) or Write (0) operation. The
    following 7 bits contain the Register Address. In cases of multiple-byte Read/Writes, data is two
    or more bytes:
    
    """
    
    def readAK(self, reg):
        self.write_reg(I2C_SLV0_ADDR, AK8963_I2C_ADDR | I2C_READ_FLAG)
        self.write_reg(I2C_SLV0_REG, reg)
        self.write_reg(I2C_SLV0_CTRL,I2C_SLV0_EN | 0x01)
        sleep_ms(1)
        self.read_reg(EXT_SENS_DATA_00)
    
    def spi_read(self, register):
        self.mpuActive()
        self.buff_r[0] = register | READ_CMD
        self.sens.write(self.buff_r)
        self.data_recv = self.sens.read(2)
        self.mpuDisable()
        
        return True
        
        
    def read_reg(self, register):
        if self.spi_read(register):
            
            print("[SPI-R] data recv is: ", hex(self.data_recv[0]))
        else:
            print("Error in read.")
            
            
    def write_reg(self, register, data):
        # Represent the int register in byte info.
        if self.spi_write(data, register):
            pass
        else:
            print("Error in write.")
            
        
    
    
    
    
    
MPU9250()
print("pepe")

