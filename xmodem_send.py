from xbee_driver import xbee_driver as XBee

RPi_sender = XBee()

imgFile = open('/home/pi/Documents/OTIS-2U-Repo/images/test.png', 'rb')
RPi_sender.send(imgFile)
