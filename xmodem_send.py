from xbee_driver import xbee_driver as XBee

RPi_XBee = XBee()

RPi_XBee.putc("active ")

i = 0
while i <= 10:
    RPi_XBee.putc(str(i))
    i += 1

#stream = open()
#modem.send(stream)
