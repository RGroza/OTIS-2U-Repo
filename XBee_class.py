import serial
from time import sleep
import os

class XBee:
    def __init__(self, serial_port, baud): #serial port as string, baud rate as int
        self.ser = serial.Serial(
            port=serial_port,
            baudrate = baud,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
         )

    def send_file(self, filepath): #filepath as string
        stream = open(filepath, 'rb')
        data = stream.read()

        fileSize = os.path.getsize(filepath)
        self.ser.write(fileSize.to_bytes(2, byteorder="big", signed=False))
        print(fileSize.to_bytes(2, byteorder="big", signed=False))
        print(fileSize)

        self.ser.write(data)
        sleep(2)

        iniFileSize = fileSize

        while fileSize > 0:
            fileSize = self.ser.outWaiting()
            self.update_progress(int(((iniFileSize - fileSize) / iniFileSize) * 100))

    def rec_file(self, filepath): #filepath as string
        print('Idle...')

        fileSize = 0
        receivedBytes = 0

        while True:
            rec = self.ser.read()
            if receivedBytes >= 2: # or rec == b''
                break
            elif not rec == b'':
                receivedBytes += 1
                fileSize = fileSize * 256 + int.from_bytes(rec, byteorder="little")

        if fileSize == 0:
            print("No file received! Exiting...")
            return

        stream = open(filepath, 'wb')
        received = False

        print("Reading file... " + str(fileSize) + " bytes")
        
        iniFileSize = fileSize

        while fileSize > 0:
            rec = self.ser.read()
            if rec == b'' and received == True:
                print("Oops!")
                break
            elif not rec == b'':
                fileSize -= 1
                received = True
                self.update_progress(int(((iniFileSize - fileSize) / iniFileSize) * 100))
                stream.write(rec)
        print(" Done!")

    def update_progress(self, progress):
        print('\r[{0}] {1}%'.format('#'*int(progress/10), progress), end="", flush=True)

    def send_cmd(self, command):
        self.ser.write(command)

    def rec_cmd(self):
        attempt_counter = 0
        eot_counter = 0
        received = False
        command = ''

        while True:
            rec = self.ser.read()
            if rec == '' and received == True:
                eot_counter += 1
            elif not rec == '':
                received = True
                command += rec
            if attempt_counter > 5 and received == False:
                break
            if eot_counter > 0:
                eot_counter = 0
                break
            attempt_counter += 1
        return command
