#hi
import picamera

class CameraClass:
  #option to use jpeg, png, bmp, gif formats
  def takePic(self, name):
    with picamera.PiCamera() as camera:
      camera.resolution = (1280,720)
      camera.capture("/home/pi/Documents/CubeSats/images/Test_Full/" + str(name) + ".png")
      camera.resolution = (128,128)
      camera.capture("/home/pi/Documents/CubeSats/images/Test_Half/" + str(name) + ".png")
    return "/home/pi/Documents/CubeSats/images/Test_Half/" + str(name) + ".png"
      
  #def resizePic(self, name):
    
