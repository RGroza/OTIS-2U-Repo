import GPSClass
import CameraClass
import ProcessClass
import time
import xbee_driver as xbee
import power_system
#import RPi.GPIO as GPIO

GPS = GPSClass.GPSClass(-1,-1,0)
camera = CameraClass.CameraClass()
inc = 0
power = power_system.power_system()
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(#insert num, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#Every ~2 minutes, reset odometer
while True: #Insert onAB() from IMU class
   #if GPIO.input(num):
    #   inc += 1
    name = camera.takePic(inc)
    if process.middlePix(name):
        if process.midRowPix(name):
            #print inc
            list = processClass.picIdentify(name)
            GPS.getGPS()
            print (list)
            xbee.send(name)
            print ("Latitude: " + GPS.getLatitude())
            print ("Longitude: " + GPS.getLongitude())
            print ("Time: " + GPS.getTime())


    print ("Battery charge: " + power.getBattPercent())
    print ("Voltage: " + power.getBattV()) #unsure if this gives voltage of solar panels
    time.sleep(0.5)
