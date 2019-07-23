from xbee_driver import xbee_driver as XBee
import base64

RPi_XBee = XBee()

def encodeImg(file):
    with open(file, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
        return str

imgFile = open('/home/pi/Documents/OTIS-2U-Repo/images/test.png', 'rb')
modem.send(imgFile)

#RPi_XBee.putc(encodeImg('/home/pi/Documents/CubeSat/images/test.png'))
