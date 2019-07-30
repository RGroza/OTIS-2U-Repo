#File for testing IMU magnetometer

import IMU

imu = IMU.IMU()

while True:
   print(imu.getDirection())
