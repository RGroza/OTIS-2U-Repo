from XBee_class import XBee

def receiveFiles(mydir, fileType='.jpg'):
    currentFile = 0
    while True:
        print("Waiting for satellite sync...")
        ground_station.wait_file_sync()
        fileStatus = True
        while fileStatus:
            fileStatus = ground_station.rec_file(mydir + str(currentFile) + fileType)
            if fileStatus:
                print("Image " + str(currentFile) + " received!")
                currentFile += 1

ground_station = XBee('COM9', 4800)

receiveFiles('C:/Work/BWSI/CubeSats/sat_images/')