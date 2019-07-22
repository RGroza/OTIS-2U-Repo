
import sys
import time
import difflib
import pigpio

class GPSClass:

    #constructor
    def __init__(self,la,lo,t):
        self.latitude=la
        self.longitude=lo
        self.time=t
    
    #gets gps data and converts to attributes
    def getGPS(self):
        RX=26
        counter = 0
        pi = pigpio.pi()
        pi.set_mode(RX, pigpio.INPUT)
        pi.bb_serial_read_open(RX, 9600, 8)
        while 1:
            (count, data) = pi.bb_serial_read(RX)
            if count:
                    self.latitude = la
                    self.longitude = lo
                    self.time = t
            time.sleep(1)

    def getLatitude(self):
        return str(self.latitude) 

    def getLongitude(self):
        return str(self.longitude) 

    def getTime(self):
        return str(self.time) 
