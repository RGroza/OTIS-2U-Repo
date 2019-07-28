from XBee_class import XBee

mydir = '/home/pi/Documents/OTIS-2U-Repo/images/test.png'

satellite = XBee('/dev/ttyUSB0', 9600)

satellite.send_file(mydir)

print("File sent!")