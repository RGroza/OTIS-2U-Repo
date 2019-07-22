from xbee_driver import xbee_driver as XBee

RPi_XBee = XBee()

imgFile = open('test.png', 'wb')
modem.recv(imgFile)