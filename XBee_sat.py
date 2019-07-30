from XBee_class import XBee
from PIL import Image
from time import sleep
from os import listdir
from os.path import isfile, join

def convert_to_jpg(file): # filepath as string
    im = Image.open(file)
    jpg_im = im.convert('RGB')
    jpg_im.save(file[0:file.index('.')] + '.jpg', quality=70)

# sends the first n files after the previously sent file
def sendFileBatch(mydir, filesNum, prevType='.png', convType='.jpg', textType='.txt'): # n -> number of images as int, fileType as string '.jpg'
    satellite.start_file_sync()
    for n in range(filesNum):
        print("Converting image " + str(n))
        convert_to_jpg(mydir + str(n) + prevType)
        print("Image converted, sending image")
        satellite.send_file(mydir + str(n) + convType, convType)
        print("Image sent!")
        satellite.send_file(mydir + str(n) + textType, textType)

def collectFiles(mydir, archivedir):
        onlyfiles = [f for f in listdir(mydir) if isfile(join(mydir, f))]
        onlyfiles.sort()
        for fileName in onlyfiles:
                if fileName.endswith(".png"):
                        print("Converting image: " + fileName)
                        convert_to_jpg(mydir + fileName)
                        print("Archiving file: " + fileName)
                        os.rename(mydir + fileName, archivedir + fileName)
                        fileName = filename.replace(".png", ".jpg")
                print("Sending file: " + fileName)
                satellite.send_file(mydir, fileName)
                print("Archiving file: " + fileName)
                os.rename(mydir + fileName, archivedir + fileName)

satellite = XBee('/dev/ttyUSB0', 4800)

#sendFileBatch('/home/pi/Documents/OTIS-2U-Repo/images/', 5)
collectFiles('/home/pi/Documents/OTIS-2U-Repo/images/', '/home/pi/Documents/OTIS-2U-Repo/archived/')

print("Files sent!")