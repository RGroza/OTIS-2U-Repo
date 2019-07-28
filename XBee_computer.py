from XBee_class import XBee

class XBee_computer:

    mydir = 'C:/Work/BWSI/CubeSats/images/'
    currentFile = 0

    def receiveFiles(fileType='.jpg'):
        ground_station.rec_file(mydir + str(currentFile) + fileType)
        print("Image " + currentFile + " received!")
        currentFile += 1

ground_station = XBee('COM9', 4800)

receiveFiles()