from XBee_class import XBee

mydir = 'C:/Work/BWSI/CubeSats/images/test.png'

ground_station = XBee('COM9', 9600)

ground_station.rec_file(mydir)

print("File received!")