#code to send a file over XBee RF module using the xmodem file transfer pro$
import serial
import time
from xmodem import XMODEM
import logging
logging.basicConfig()

class xbee_driver:

    #creates ser and modem. modem is used for sending files, while ser is used for direct access
    #to what the XBee is sending.
    def __init__(self):
        self.ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        self.modem = XMODEM(self.getc, self.putc)
    #both getc and putc are only used for passing to XMODEM, will not be used by client.

    def getc(self, size, timeout=1):
        return self.ser.read(size) or None

    def putc(self, data, timeout=1):
        return self.ser.write(data)

    #this file should be called on the CubeSat, and is used for sending any file.
    #file is a string file directory of what is being sent.
    def send(self, file):
        stream = open(file, 'rb')
        self.modem.send(stream)

    #requests a file and saves it in savelocation. This method does not return anything.
    #to access the requested file it must be called after the request method.
    #both file and savelocation are string file directories
    def request(self, file, savelocation):
        sendcommand("get")
        sendcommand(file)
        time.sleep(5)
        stream = open(savelocation, 'wb')
        self.modem.recv(stream)

    def receive(self, savelocation):
        stream = open(savelocation, 'wb')
        self.modem.recv(stream)

    #used for commands and when the client wants to send data directly rather than as a file.
    #cmd = "get" is reserved for requesting a file.
    def sendcommand(self, cmd):
        self.ser.write(cmd)

    #used for interpretting commands sent by sendcomand
    def readcommand(self):
        return self.ser.readline()
