#Takes pic and processes it
from PIL import Image
import os

class ProcessClass1:

  #Checks the middle pixel to see if it is green 
  #If so, it deletes the image and returns False
  #else returns True
  def middlePix(self, name):
    image=Image.open(name)
    pixel=image.load()
    j=56
    k=56
    count=0
    while j<72:
      while k<72:
        pix=pixel[j,k]
        if not (pix[0]<200 and pix[0]>100 and pix[1]<255 and pix[1]>100 and pix[2]<160 and pix[2]>50):
          count+=1
        k+=1
      k=0
      j+=1
    if count<200:
      #os.remove(name)
      return False
    else:
      return True
  
  #checks the middle row of pixels
  #should be called after the middlePix method
  #returns true or false
  def midRowPix(self, name):
    image=Image.open(name)
    pixel=image.load()
    count=0
    count1=0
    while count<10:
      pix=pixel[count,64]
      if not (pix[0]<50 and pix[0]>25 and pix[1]<80 and pix[1]>25 and pix[2]<30):
        count1+=1
      count+=1
    if count1<6:
      #os.remove(name)
      return False
    count1=0
    count=56
    print ("hi1")
    while count<72:
      pix=pixel[count,64]
      if pix[0]<50 and pix[0]>25 and pix[1]<80 and pix[1]>25 and pix[2]<30:
        #os.remove(name)
        return False
      count+=1
    count=117
    print ("hi2")
    while count<128:
      pix=pixel[count,64]
      if not (pix[0]<50 and pix[0]>25 and pix[1]<80 and pix[1]>25 and pix[2]<30):
        count1+=1
      count+=1
    if count1<6:
      #os.remove(name)
      return False
    print ("hi3")
    return True
  
  #runs through and spices the pixels
  #returns a list containing:
  #oxi to all pix, oil to all pix, oxi to oil, oxi to all oil, oil to all oil
  def picIdentify(self, name):
    image=Image.open(name)
    pixel=image.load()
    j=0
    k=0
    oxi=0
    oil=0
    while j<128:
      while k<128:
        pix=pixel[j,k]
        #if not ((pix[0]<50 and pix[0]>25 and pix[1]<80 and pix[1]>25 and pix[2]<30) or (pix[0]>120 and pix[1]>120 and pix[2]>120)):
        if ((pix[0]>75 and pix[0]<195) and (pix[1]<155 and pix[1]>30) and (pix[2]<35)):
            oxi+=1
        if (pix[0]<100 and pix[1]<100 and pix[2]<100):
            oil+=1
        k+=1
      k=0
      j+=1
    return self.calculate(oxi,oil)
  
  #embeded method used in picIdentify
  def calculate(self,ox,oi):
    perAllOxi=float(ox)/1048576
    perAllOil=float(oi)/1048576
    oxiOil=ox+oi
    if oxiOil==0:
      return 0.0
    perOxi=float(ox)/oxiOil
    perOil=float(oi)/oxiOil
    holder=perOxi*100
    return holder
  
  def determineEffectiveness(self, holder):
    if holder <= 45:
      return True
    else:
      return False
  
