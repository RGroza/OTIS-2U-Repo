import serial
from time import sleep
import time
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

    def wait_file_sync(self, timeout=False):
        print('Waiting for X byte...')

        receivedByte = False

        if timeout:
            beginTime = time.time()
            while time.time() - beginTime <= 5:
                rec = self.ser.read()
                if receivedByte == True:
                    return
                elif not rec == b'':
                    receivedByte = True
            self.start_file_sync()
        else:
            while True:
                rec = self.ser.read()
                if receivedByte == True:
                    return
                elif not rec == b'':
                    receivedByte = True

    def start_file_sync(self):
        self.ser.write(b'x')
        print("X byte sent!")

    def send_file(self, fileDir, fileName):
        stream = open(fileDir + fileName, 'rb')
        data = stream.read()

        fileSize = os.path.getsize(fileDir + fileName)
        self.wait_file_sync()
        self.ser.write(fileSize.to_bytes(2, byteorder="big", signed=False))
        print(fileSize)

        fileNameLen = len(fileName)
        self.wait_file_sync()
        self.ser.write(fileNameLen.to_bytes(1, byteorder="big", signed=False))
        print("fileNameLen")

        self.wait_file_sync()
        self.ser.write(fileName.encode())
        print("fileName")

        self.wait_file_sync()
        self.ser.write(data)
        print("File sent")

    def rec_file(self, fileDir): #, batchNum):
        self.start_file_sync()
        print('Starting receiving procedure...')

        fileSize = 0
        receivedBytes = 0

        beginTime = time.time()
        while True:
            rec = self.ser.read()
            if receivedBytes >= 2: # or rec == b''
                break
            elif not rec == b'':
                receivedBytes += 1
                fileSize = fileSize * 256 + int.from_bytes(rec, byteorder="little")
            elif rec == b'' and time.time() - beginTime > 5:
                print("No data found! (fileSize)")
                return False

        if fileSize == 0:
            print("0 file size! Exiting...")
            return False

        fileNameLen = 0
        receivedBytes = 0

        self.start_file_sync()

        beginTime = time.time()
        while True:
            rec = self.ser.read()
            if receivedBytes >= 1: # or rec == b''
                break
            elif not rec == b'':
                receivedBytes += 1
                fileNameLen = fileNameLen * 256 + int.from_bytes(rec, byteorder="little")
                # print(rec)
            elif rec == b'' and time.time() - beginTime > 5:
                print("No data found! (fileNameLen)")
                return False

        if fileNameLen == 0:
            print("0 file name length! Exiting...")
            return False

        fileName = ""
        receivedBytes = 0

        self.start_file_sync()

        beginTime = time.time()
        while True:
            rec = self.ser.read()
            if receivedBytes >= fileNameLen: # or rec == b''
                break
            elif not rec == b'':
                receivedBytes += 1
                fileName += rec.decode()
            elif rec == b'' and time.time() - beginTime > 5:
                print("No data found! (fileName)")
                return False

        if len(fileName) != fileNameLen:
            print("Invalid file name! Exiting...")
            return False

        self.start_file_sync()

        stream = open(fileDir + fileName, 'wb')
        received = False

        print("Reading file... (" + fileName + ") " + str(fileSize) + " bytes")
        
        iniFileSize = fileSize

        self.start_file_sync()
        
        rec_complete = True
        while fileSize > 0:
            rec = self.ser.read()
            if rec == b'' and received == True:
                recovered = False
                beginTime = time.time()
                while time.time() - beginTime <= 5: # recover downlink if connection is lost
                    if not rec == b'':
                        fileSize -= 1
                        received = True
                        self.update_progress(int(((iniFileSize - fileSize) / iniFileSize) * 100))
                        stream.write(rec)
                        recovered = True
                        rec_complete = False
                        break
                if not recovered:
                    print(" Oops!")
                    break
            elif not rec == b'':
                fileSize -= 1
                received = True
                self.update_progress(int(((iniFileSize - fileSize) / iniFileSize) * 100))
                stream.write(rec)
        if rec_complete:
            print(" Image " + fileName + " received!")

        return True

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
