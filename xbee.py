import serial
from time import sleep

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
        self.ser.write(data)

    def rec_file(self, filepath): #filepath as string
        stream = open(filepath, 'ab')
        eot_counter = 0
        received = False

        while True:
            print('receiving')
            rec = self.ser.read()
            print(rec)
            if rec == '' and received == True:
                eot_counter += 1
            elif not rec == '':
                received = True
                stream.write(rec)
            if eot_counter > 0:
                eot_counter = 0
                break

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
