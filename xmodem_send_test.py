import time
import serial
from xmodem import XMODEM
import logging
logging.basicConfig()

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def getc(size, timeout=1):
    return ser.read(size) or None

def putc(data, timeout=1):
    return ser.write(data)

modem = XMODEM(getc, putc)

stream = open('/images/test.png', 'rb')
modem.send(stream)
