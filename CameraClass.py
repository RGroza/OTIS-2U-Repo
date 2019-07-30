#hi
import picamera
from time import sleep

class CameraClass:
  #option to use jpeg, png, bmp, gif formats
  def takePic(self, name):
    with picamera.PiCamera() as camera:
      camera.iso = 100
      sleep(2)
      camera.shutter_speed = camera.exposure_speed
      camera.exposure_mode = 'off'
      g = camera.awb_gains
      camera.awb_mode = 'off'
      camera.awb_gains = g
      #camera.resolution = (1024,1024)
      #camera.capture("/home/pi/CubeSats/High" + str(name) + ".png")
      camera.resolution = (128,128)
      camera.capture("/home/pi/CubeSats/Low" + str(name) + ".png")
    return "/home/pi/CubeSats/Low" + str(name) + ".png"
  
  def calTakePic(self, name):
    with picamera.PiCamera() as camera:
      camera.iso = 100
      sleep(2)
      camera.shutter_speed = camera.exposure_speed
      camera.exposure_mode = 'off'
      g = camera.awb_gains
      camera.awb_mode = 'off'
      camera.awb_gains = g
      camera.resolution = (1024,1024)
      camera.capture("/home/pi/Calibrate/" + str(name) + ".png")
    return "/home/pi/Calibrate/" + str(name) + ".png"
  #def resizePic(self, name):
   
