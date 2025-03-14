#import GPSClass
import CameraClass
import ProcessClass
import time
import XBee_sat
import power_system
import temp_monitor
import IMU
import math
import RPi.GPIO as GPIO
#initialize objects for camera and telemetry
#GPS = GPSClass.GPSClass(-1,-1,0)
distance = 0
camera = CameraClass.CameraClass()
power = power_system.power_system()
process = ProcessClass.ProcessClass()
#imu=IMU.IMU()
#cal=Calibrate.Calibrate()
#sets up odometer reading
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#used for deboduncing the GPIO input
lastValue = GPIO.input(5)
counter = 0
inc = 0
count = 0
increment = 1
roberto = 0
while True: #imu.getDirection() == "N":
   telemetry = open("/home/pi/Documents/OTIS-2U-Repo/images/telemetry.txt", "w")
   while count < 7 and roberto <= 3: #imu.getDirection() == "N":
      #Picamera takes an image
      #telemetry = open("/home/pi/Documents/OTIS-2U-Repo/images/telemetry" + str(count) + ".txt", "a")
      name = camera.takePic(inc)
      if GPIO.input(5) is not lastValue:
          lastValue = GPIO.input(5)
          counter+=1
                  #prints out the amount of distance OTIS has travelled by calculating the circumference of the rotations
          distance = str((counter * (0.055 * math.pi)))
      #Determines if the image encompasses the pan
      #if process.middlePix(name) and process.midRowPix(name):
      list = process.picIdentify(name)
               #Grabs the GPS telemetry data
               #GPS.getGPS()
               #Prints out oxidation rate
      telemetry.write(str(list) + "\n")
      telemetry.write(str(distance) + "\n")
               #Returns if dispersants would be effective
               #print process.determineEffectiveness(list)
               #Sends image to ground station
               #telemetry = open("telemetry0.txt","a")
      confirm = "Picture " + str(inc) + " taken!"
      temp = temp_monitor.measure_temp()
               #lat = "Latitude: " + GPS.getLatitude()
               #lon = "Longitude: " + GPS.getLongitude()
               #GPS_time = "Time: " + GPS.getTime()
      buffer = "----------------------------"
      batt_charge = str(power.getBattPercent())
      sol_voltage_1 = str(power.getPanelXPlusV())
      sol_voltage_2 = str(power.getPanelXMinusV())
      sol_voltage_3 = str(power.getPanelYPlusV())
      sol_voltage_4 = str(power.getPanelYMinusV())
      telemetry.write(str(inc) + "\n")
      #telemetry.write(str(list))
      #telemetry.write(temp)
               #telemetry.write(lat)
               #telemetry.write(lon)
               #telemetry.write(GPS_time)
     # telemetry.write(batt_charge)
      #telemetry.write(sol_voltage_1)
      #telemetry.write(sol_voltage_2)
      #telemetry.write(sol_voltage_3)
      #telemetry.write(sol_voltage_4)
          #telemetry.write(str(distance))
               #telemetry.readlines()
      count += 1
      #Deliveers telemetry data

      inc+=1
      time.sleep(0.35)
   telemetry.write(str(batt_charge) + "\n")
   telemetry.write(str(temp))
   telemetry.write(str(sol_voltage_1) + "\n")
   telemetry.write(str(sol_voltage_2) + "\n")
   telemetry.write(str(sol_voltage_3) + "\n")
   telemetry.write(str(sol_voltage_4) + "\n")
   telemetry.close()
   XBee_sat.send_files()
   increment += 1
   count = 0
   #while imu.getDirection() != "N":
   roberto += 1
      #telemetry.close()
      #XBee_sat.send_files()
   #Calibration
   #w#hile imu.getDirection()=="SE":
    #  inc=0
      #name = camera.calTakePic(inc)
      #if process.middlePix(name):
       #  if process.midRowPix(name):
        #    cal.calGreen()
         #   cal.calOrange()
          #  cal.calBlack()
