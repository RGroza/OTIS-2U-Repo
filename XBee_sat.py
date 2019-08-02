from XBee_class import XBee
from PIL import Image
from time import sleep
import os
from os import listdir
from os.path import isfile, join
import RPi.GPIO as GPIO

def convert_to_jpg(file): # filepath as string
    im = Image.open(file)
    jpg_im = im.convert('RGB')
    jpg_im.save(file[0:file.index('.')] + '.jpg', quality=70)

def collectFiles(mydir, archivedir):
        onlyfiles = [f for f in listdir(mydir) if isfile(join(mydir, f))]
        onlyfiles.sort()
        satellite.start_file_sync()
        for fileName in onlyfiles:
                if fileName.endswith(".png"):
                        print("Converting image: " + fileName)
                        convert_to_jpg(mydir + fileName)
                        print("Archiving file: " + fileName)
                        os.rename(mydir + fileName, archivedir + fileName)
                        fileName = fileName.replace(".png", ".jpg")
                print("Sending file: " + fileName)
                satellite.send_file(mydir, fileName)
                print("Archiving file: " + fileName)
                os.rename(mydir + fileName, archivedir + fileName)

def send_files():
        collectFiles('/home/pi/Documents/OTIS-2U-Repo/images/', '/home/pi/Documents/OTIS-2U-Repo/archived/')
        print("Files sent!")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)

satellite = XBee('/dev/ttyAMA0', 115200) # '/dev/ttyUSB0', '/dev/ttyS0' or '/dev/ttyAMA0'

send_files()