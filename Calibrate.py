from PIL import Image
import os

class Calibrate:
  
  def calGreen(self, name):
    image=Image.open(name)
    pixel=image.load()
    self.green = pixel[x,x]
    
  def calOrange(self, name):
    image=Image.open(name)
    pixel=image.load()
    self.orange = pixel[x,x]
  
  def calBlack(self, name):
    image=Image.open(name)
    pixel=image.load()
    self.black = pixel[x,x]
    
  def getCalGreen(self):
    return self.green
  
  def getCalOrange(self):
    return self.orange
  
  def getCalBlack(self):
    return self.black
