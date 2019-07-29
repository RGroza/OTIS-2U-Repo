import GPSClass
import CameraClass
import ProcessClass
import time
import xbee_driver as xbee
import power_system
import temp_monitor
import IMU
import Calibrate
import Math
import RPi.GPIO as GPIO
#initialize objects for camera and telemetry
GPS = GPSClass.GPSClass(-1,-1,0)
camera = CameraClass.CameraClass()
power = power_system.power_system()
process = ProcessClass.ProcessClass()
imu=IMU.IMU()
cal=Calibrate.Calibrate()
#sets up odometer reading
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#used for deboduncing the GPIO input
lastValue = GPIO.input(5)
while True: 
   #Determines if OTIS is on the leg with the pans to take pictures
   while imu.getDirection()=="N":
      inc=0
      #Picamera takes an image
      name = camera.takePic(inc)
      #Determines if the image encompasses the pan
      if process.middlePix(name):
         if process.midRowPix(name):
               #print inc
               #Identifies the oxidation amount of the pans
               list = processClass.picIdentify(name)
               #Grabs the GPS telemetry data
               GPS.getGPS()
               #Prints out oxidation rate
               print (list)
               #Returns if dispersants would be effective
               print process.determineEffectiveness(list)
               #Sends image to ground station
               xbee.send(name)
               telemetry = open("telemetry0.txt","a")
               temp = "Temperature: " + temp_monitor.measure_temp()
               lat = "Latitude: " + GPS.getLatitude()
               lon = "Longitude: " + GPS.getLongitude()
               time = "Time: " + GPS.getTime()
               buffer = "----------------------------"
               batt_charge = "Battery charge: " + str(power.getBattPercent())
               batt_voltage = "Battery Voltage: " + str(power.getBattV())
               sol_voltage = "Solar Panel Voltage: " + str(power.getPanelXPlusV() + power.getPanelXMinusV() + power.getPanelYPlusV() + power.getPanelYMinusV())
               telemetry.write(temp)
               telemetry.write(lat)
               telemetry.write(lon)
               telemetry.write(time)
               telemetry.write(batt_charge)
               telemetry.write(batt_voltage)
               telemetry.write(sol_voltage)
               telemetry.write(buffer)
               telemtry.readlines()
               
               if GPIO.input(5) is not lastValue:
                  lastValue = GPIO.input(5)
                  counter+=1
                  #prints out the amount of distance OTIS has travelled by calculating the circumference of the rotations
                  print ("Distance travelled: " + (counter * (0.055 * Math.pi)))

      #Deliveers telemetry data
      time.sleep(0.30)
      inc+=1
   #Calibration
   while imu.getDirection()=="SE":
      inc=0
      name = camera.calTakePic(inc)
      if process.middlePix(name):
         if process.midRowPix(name):
            cal.calGreen()
            cal.calOrange()
            cal.calBlack()
            
            
