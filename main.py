import GPSClass
import CameraClass
import ProcessClass as process
import XBee_driver as xbee


GPS = GPSClass.GPSClass(-1,-1,0)
camera = CameraClass.CameraClass()
inc = 0
while 1 #Insert onAB() from IMU class:
    #insert camera taking picture
    camera.takePic(inc)
    if process.middlePix(name):
        if process.midRowPix(name):
            GPS.getGPS()
            print process.picIdentify(name)
            xbee.send(name)
            print "Latitude: " + GPS.getLatitude()
            print "Longitude: " + GPS.getLongitude()
            print "Time: " + GPS.getTime()
            


    inc += 1
    time.sleep(0.5)
