import smbus
import time
import math
import numpy as np
import ctypes

class IMU:
	bus=smbus.SMBus(1)
	address=0x1e
	whoami=bus.read_byte_data(address, 0x0f)

	#enable magnetometer
	bus.write_byte_data(address, 0x21, 0x40)
	bus.write_byte_data(address, 0x20, 0xfc)
	bus.write_byte_data(address, 0x23, 0x0c)
	bus.write_byte_data(address, 0x22, 0x00)

	def getDirection(self):
		statusReg=bus.read_byte_data(address, 0x27)

		#magXLow=bus.read_byte_data(address, 0x28)
		magXHigh=bus.read_byte_data(address, 0x29)
		#magYLow=bus.read_byte_data(address,0x2a)
		magYHigh=bus.read_byte_data(address, 0x2b)

		gaussnum=1.0/2281
		x16=(magXHigh << 8)
		y16=(magYHigh << 8)
		xNew=ctypes.c_short(x16).value
		yNew=ctypes.c_short(y16).value

		xGaussData=xNew*gaussnum
		yGaussData=yNew*gaussnum

		direction=math.atan2(yGaussData, xGaussData)*(180/np.pi)

		if direction <0:
			direction+=360

		if direction>55 and direction <110:
			return "N"
		#	print("north", direction)
		elif direction > 290 and direction < 330:
			return "SE"
		#	print("se, leg ab", direction)
		elif direction >200  and direction <235:
			return "SW"
		#	print("sw, leg bc",direction)
		else: print("no")

		time.sleep(.5)


