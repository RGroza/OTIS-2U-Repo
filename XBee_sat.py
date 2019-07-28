from XBee_class import XBee
from PIL import Image
from time import sleep

def convert_to_jpg(file): # filepath as string
    im = Image.open(file)
    jpg_im = im.convert('RGB')
    jpg_im.save(file[0:file.index('.')] + '.jpg', quality=70)

# sends the first n files after the previously sent file
def sendFileBatch(mydir, filesNum, prevType='.png', convType='.jpg'): # n -> number of images as int, fileType as string '.jpg'
    for n in range(filesNum):
        print("Converting image " + str(n))
        convert_to_jpg(mydir + str(n) + prevType)
        print("Image converted, sending image")
        satellite.send_file(mydir + str(n) + convType)
        print("Image sent!")

satellite = XBee('/dev/ttyUSB0', 4800)

sendFileBatch('/home/pi/Documents/OTIS-2U-Repo/images/', 1)

print("Files sent!")