from xmodem import XMODEM
import time
import serial
import logging
from pathlib import Path

logging.basicConfig()

#open the serial connection to the XBee. Change the baud rate and port as necessary.
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 38400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS,
    timeout=1
 )

#define sending and receiving for XModem. Don't worry about it.
def getc(size, timeout=1):
    return ser.read(size) or None

def putc(data, timeout=1):
    return ser.write(data)

modem = XMODEM(getc, putc)

client_connected = True
tx_count = 0
pic_tx_count = 0

while True:
    stream = open('parameters', 'wb') #open the parameter input file. Change this path to your parameter file.
    client_connected = modem.recv(stream)

    #don't try to send if there is no connection to the ground station. will revert to trying to contact the ground station.
    if not client_connected == None and not client_connected == False:
        if tx_count % 2 == 0:
            stream = open('telemetry', 'rb') #open the telemetry receive file. Change this path to your telemetry file.
            client_connected = modem.send(stream)
            time.sleep(2)
        else:
            pic_path = 'pics/pic' + str(pic_tx_count)
            pic = Path(pic_path)
            if pic.is_file():
                stream = open(pic_path, 'rb')
                client_connected = modem.send(stream)
                pic_tx_count += 1
                time.sleep(2)
            else:
                stream = open('telemetry', 'rb') #open the telemetry receive file. Change this path to your telemetry file.
                client_connected = modem.send(stream)
                time.sleep(2)
        tx_count += 1
