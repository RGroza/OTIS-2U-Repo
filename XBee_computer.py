from XBee_class import XBee

def receiveFiles(mydir, fileType='.jpg'):
    batchNum = 0
    while True:
        batchNum += 1
        print("Waiting for satellite sync...")
        ground_station.wait_file_sync()
        fileStatus = True
        while fileStatus:
            fileStatus = ground_station.rec_file(mydir)

ground_station = XBee('COM9', 9600)

receiveFiles('C:/Work/BWSI/CubeSats/sat_images/')