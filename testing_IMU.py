#File for testing IMU magnetometer

import IMU

imu = IMU.IMU()

while True:
   if imu.getDirection() == "N":
      print("Pointing North!")
