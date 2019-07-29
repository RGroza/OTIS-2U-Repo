from XBee_class import XBee

def receiveFiles(mydir, fileType='.jpg'):
    currentFile = 0
    print("Waiting for satellite sync...")
    ground_station.wait_file_sync()
    while True:
        ground_station.rec_file(mydir + str(currentFile) + fileType)
        print("Image " + str(currentFile) + " received!")
        currentFile += 1

ground_station = XBee('COM9', 4800)

receiveFiles('C:/Work/BWSI/CubeSats/sat_images/')