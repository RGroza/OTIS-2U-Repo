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
        (count, data) = pi.bb_serial_read(RX)
        gained = False
        while gained != True:
           if count:
               new_data = str(data, 'utf-8')
               for line in new_data.split('\n') :
                    if line.startswith( '$GPGGA' ):
                        context = line.strip().split(',')
                        lat_line = context[2]
                        lon_line = context[4]
                        self.latitude = lat_line[0:2] + "." + lat_line[2:4]
                        self.longitude = lon_line[0:3] + "." + lon_line[3:5]
                        self.time = context[1]
                        gained = True
           time.sleep(0.5)
        pi.bb_serial_read_close(RX)
        pi.stop()

    def getLatitude(self):
        return str(self.latitude) 

    def getLongitude(self):
        return str(self.longitude) 

    def getTime(self):
        return str(self.time) 
