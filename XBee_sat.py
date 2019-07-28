from XBee_class import XBee
from time import sleep

class XBee_sat:

    mydir = '/home/pi/Documents/OTIS-2U-Repo/images/'
    currentFile = 0
    JPG_quality = 95

    def convert_to_JPG(file): # filepath as string
        im = Image.open(file)
        bg = Image.new('RGB', im.size, (255,255,255))
        bg.paste(im, (0,0), im)
        bg.save(file[0:file.index('.')] + '.jpg', quality=JPG_quality)

    # sends the first n files after the previously sent file
    def sendFileBatch(n, prevFileType='.png', convertedFileType='.jpg'): # n -> number of images as int, fileType as string '.jpg'
        for in range(n):
            print("Converting image " + str(n))
            convert_to_JPG(str(n) + prevFileType)
            print("Image converted, sending image")
            satellite.send_file(mydir + str(currentFile) + convertedFileType)
            print("Image sent!")
            currentFile += 1
            sleep(0.1)

satellite = XBee('/dev/ttyUSB0', 9600)

sendFileBatch(5)

print("Files sent!")