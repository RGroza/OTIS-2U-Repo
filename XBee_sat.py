from xbee import XBee
from PIL import Image
from time import sleep

def convert_to_jpg(file): # filepath as string
    im = Image.open(file)
    jpg_im = im.convert('RGB')
    jpg_im.save(file[0:file.index('.')] + '.jpg', quality=80)

# sends the first n files after the previously sent file
def sendFileBatch(mydir, filesNum, prevFileType='.png', convertedFileType='.jpg'): # n -> number of images as int, fileType as string '.jpg'
    for n in range(filesNum):
        #print("Converting image " + str(n))
        #convert_to_jpg(mydir + str(n) + prevFileType)
        #print("Image converted, sending image")
        satellite.send_file(mydir + 'test' + str(n) + convertedFileType)
        print("Image sent!")
        sleep(2)

satellite = XBee('/dev/ttyUSB0', 9600)

sendFileBatch('/home/pi/Documents/OTIS-2U-Repo/images/', 4)

print("Files sent!")