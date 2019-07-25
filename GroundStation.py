from xmodem import XMODEM
import time
import serial
import logging

pic_counter = 0

logging.basicConfig()

#open the serial connection to the XBee. Change the baud rate and port as necessary.
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 38400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
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

while True:
    #look for a client
    stream = open('/home/max/Desktop/CubeSat/SLOOP_REC/parameters', 'rb') #open the parameter input file. Change this path to your parameter file.
    client_connected = modem.send(stream) #wait for a connection
    print(client_connected)

    time.sleep(2)

    #don't attempt to retrieve satellite data if it didn't connect. ground station will go back to its initial state of waiting for a connection.
    if not client_connected == None and not client_connected == False:
        #retrieve data and store it in a temporary receive file.
        stream = open('/home/max/Desktop/CubeSat/SLOOP_REC/temp', 'wb') #open the temporary receive location. Change this path to your temp file.
        client_connected = modem.recv(stream) #will be None if no client is connected
        stream = open('/home/max/Desktop/CubeSat/SLOOP_REC/temp', 'r')
        data = stream.readlines()
        if not client_connected == None: #just make extra sure that we received data before reading so we don't try to read an empty file.
            print(data[0])
            if data[0] == "telemetry\n":
                stream = open('/home/max/Desktop/CubeSat/SLOOP_REC/temp', 'r')
                destination = open('/home/max/Desktop/CubeSat/SLOOP_REC/telemetry', 'w')
                destination.write(stream.read())
            else:
                #store anything else to a new file each time, instead of overwriting.
                dest_location = '/home/max/Desktop/CubeSat/SLOOP_REC/Images/pic'
                dest_location += str(pic_counter)
                stream = open('/home/max/Desktop/CubeSat/SLOOP_REC/temp', 'r')
                destination = open(dest_location, 'w')
                destination.write(stream.read())
                pic_counter += 1
            
