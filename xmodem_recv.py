from xbee_driver import xbee_driver as XBee

RPi_sender = XBee()

RPi_sender.recv('/home/pi/Documents/OTIS-2U-Repo/images/test.png')
