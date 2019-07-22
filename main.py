import GPSClass
import CameraClass
import ProcessClass
import time
import xbee_driver as xbee
import power_system

GPS = GPSClass.GPSClass(-1,-1,0)
camera = CameraClass.CameraClass()
process = ProcessClass.ProcessClass()
inc = 0
power = power_system.power_system()
#Every ~2 minutes, reset odometer
while True: #Insert onAB() from IMU class
    name = camera.takePic(inc)
    if process.middlePix(name):
        if process.midRowPix(name):
            list = process.picIdentify(name)
            GPS.getGPS()
            print (list)
            xbee.send(name)
            print ("Latitude: " + GPS.getLatitude())
            print ("Longitude: " + GPS.getLongitude())
            print ("Time: " + GPS.getTime())


    print ("Battery charge: " + power.getBattPercent())
    print ("Voltage: " + power.getBattV()) #unsure if this gives voltage of solar panels
    inc += 1
    time.sleep(0.5)
