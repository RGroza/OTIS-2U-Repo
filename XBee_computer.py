from xbee import XBee

def receiveFiles(mydir, fileType='.jpg'):
    currentFile = 0
    while True:
        ground_station.rec_file(mydir + 'test' + str(currentFile) + fileType)
        print("Image " + 'test' + str(currentFile) + " received!")
        currentFile += 1

ground_station = XBee('COM9', 4800)

receiveFiles('C:/Work/BWSI/CubeSats/sat_images/')