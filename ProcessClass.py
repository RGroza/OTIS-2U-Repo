#Takes pic and processes it
from PIL import Image
import os

class ProcessClass:

  #Checks the middle pixel to see if it is green 
  #If so, it deletes the image and returns False
  #else returns True
  def middlePix(self, name):
    image=Image.open(name)
    coord=(64,64)
    pix=image.getpixel(coord)
    if pix[1]>100 and pix[0]<100 and pix[2]<50:
      os.remove(name)
      return False
    else:
      return True
  
  #checks the middle row of pixels
  #should be called after the middlePix method
  #returns true or false
  def midRowPix(self, name):
    image=Image.open(name)
    count=0
    #while count<10:
      #coord=(count,64)
      #pix=image.getpixel(coord)
      #if not (pix[1]>100 and pix[0]<100 and pix[2]<50):
        #os.remove(name)
        #return False
      #count+=1
    count=58
    while count<70:
      coord=(count,64)
      pix=image.getpixel(coord)
      if pix[1]>100 and pix[0]<100 and pix[2]<50:
        os.remove(name)
        return False
      count+=1
    count=117
    #while count<128:
      #coord=(count,64)
      #pix=image.getpixel(coord)
      #if not (pix[1]>100 and pix[0]<100 and pix[2]<50):
        #os.remove(name)
        #return False
      #count+=1
    return True
  
  #runs through and spices the pixels
  #returns a list containing:
  #oxi to all pix, oil to all pix, oxi to oil, oxi to all oil, oil to all oil
  def picIdentify(self, name):
    image=Image.open(name)
    j=0
    k=0
    oxi=0
    oil=0
    while j<128:
      while k<128:
        coord=(j,k)
        pix=image.getpixel(coord)
        if not ((pix[1]>100 and pix[0]<100 and pix[2]<50) or (pix[0]>120 and pix[1]>120 and pix[2]>120)):
          if (pix[0]>130 and pix[1]<200 and pix[1]>70 and pix[2]<125):
            oxi+=1
          elif (pix[1]<60 and pix[0]<60 and pix[2]<60):
            oil+=1
          else:
            continue
        k+=1
      k=0
      j+=1
    return self.calculate(oxi,oil)
  
  #embeded method used in picIdentify
  def calculate(self,oxi,oil):
    perAllOxi=oxi/16384
    perAllOil=oil/16384
    oxiToOil=oxi/oil
    oxiOil=oxi+oil
    perOxi=oxi/oxiOil
    perOil=oil/oxiOil
    return perOxi
  
  
