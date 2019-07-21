#hi
import picamera

class CameraClass:
  #name must have a .jpg file tag
  def takePic(self, name):
    with picamera.PiCamera() as camera:
      camera.resolution = (1280,720)
      camera.capture("/home/pi/Test_Full/" + name + ".jpg")
      camera.resolution = (128,128)
      camera.capture("/home/pi/Test_Half/" + name + ".jpg")
      
  def resizePic(self, name):
    
