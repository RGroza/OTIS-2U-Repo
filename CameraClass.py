#hi
import picamera

class CameraClass:
  #option to use jpeg, png, bmp, gif formats
  def takePic(self, name, imgFormat):
    with picamera.PiCamera() as camera:
      camera.resolution = (1280,720)
      camera.capture("/home/pi/Documents/CubeSats/images/Test_Full/" + name + "." + imgFormat, format=imgFormat)
      camera.resolution = (128,128)
      camera.capture("/home/pi/Documents/CubeSats/images/Test_Half/" + name + "." + imgFormat, format=imgFormat)
      
  def resizePic(self, name):
    
