import GPSClass
import CameraClass
import ProcessClass
import time
#import Xbee_sat as xbee
import power_system
import temp_monitor
#import IMU
#import Calibrate
import math
import RPi.GPIO as GPIO
#initialize objects for camera and telemetry
GPS = GPSClass.GPSClass(-1,-1,0)
camera = CameraClass.CameraClass()
power = power_system.power_system()
process = ProcessClass.ProcessClass()
telemetry = open("/home/pi/Documents/OTIS-2U-Repo/images/telemetry.txt", "a")
#imu=IMU.IMU()
#cal=Calibrate.Calibrate()
#sets up odometer reading
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#used for deboduncing the GPIO input
lastValue = GPIO.input(5)
counter = 0
inc = 0
while True: 
   #Determines if OTIS is on the leg with the pans to take pictures
   while True:
      #Picamera takes an image
      name = camera.takePic(inc)
      #Determines if the image encompasses the pan
      if True:  #process.middlePix(name):
         if True: #process.midRowPix(name):
               #print inc
               #Identifies the oxidation amount of the pans
               list = process.picIdentify(name)
               #Grabs the GPS telemetry data
               GPS.getGPS()
               #Prints out oxidation rate
               print (list)
               #Returns if dispersants would be effective
               #print process.determineEffectiveness(list)
               #Sends image to ground station
               #xbee.send(name)
               #telemetry = open("telemetry0.txt","a")
               print("Temperature: " + temp_monitor.measure_temp())
               print("Latitude: " + GPS.getLatitude())
               print("Longitude: " + GPS.getLongitude())
               print("Time: " + GPS.getTime())
               #buffer = "----------------------------"
               print("Battery charge: " + str(power.getBattPercent()))
               #batt_voltage = "Battery Voltage: " + str(power.getBattV())
               #print (temp)
               #print (lat)
               #print (lon)
               #print (GPS_Time)
               #print (batt_charge)
               #print (batt_voltage)
               print ("solar voltage: " + str(power.getPanelXPlusV()))
               print ("solar voltage: " + str(power.getPanelXMinusV()))
               print ("solar voltage: " + str(power.getPanelYPlusV()))
               print ("solar voltage: " + str(power.getPanelYMinusV()))
               telemetry.write(temp)
               telemetry.write(lat)
               telemetry.write(lon)
               telemetry.write(time)
               telemetry.write(batt_charge)
               telemetry.write(batt_voltage)
               telemetry.write(sol_voltage)
               telemetry.write(buffer) 
               if GPIO.input(5) is not lastValue:
                  lastValue = GPIO.input(5)
                  counter+=1
                  #prints out the amount of distance OTIS has travelled by calculating the circumference of the rotations
                  print ("Distance travelled: " + str((counter * (0.055 * math.pi))))

      #Deliveers telemetry data
    
      inc+=1
   #Calibration
   #w#hile imu.getDirection()=="SE":
    #  inc=0
      #name = camera.calTakePic(inc)
      #if process.middlePix(name):
       #  if process.midRowPix(name):
        #    cal.calGreen()
         #   cal.calOrange()
          #  cal.calBlack()
            
            
