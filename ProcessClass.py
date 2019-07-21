#Takes pic and processes it
from PIL import Image

class ProcessClass:

  #Checks the middle pixel to see if it is green 
  #If not, it deletes the image and returns False
  #else returns True
  def middlePix(self, name):
    image=Image.open(name)
    pix=image.getpix(64,64)
    if pix[1]>100 and pix[0]<100 and pix[2]<50:
      del name
      return False
    else:
      return True
   
  def midRowPix(self, name):
    image=Image.open(name)
    count=0
    while count<10:
      pix=image.getpix(count,64)
      if not (pix[1]>100 and pix[0]<100 and pix[2]<50):
        del name
        return False
      count+=1
    count=58
    while count<70:
      pix=image.getpix(count,64)
      if pix[1]>100 and pix[0]<100 and pix[2]<50:
        del name
        return False
      count+=1
    count=117
    while count<128:
      pix=image.getpix(count,64)
      if not (pix[1]>100 and pix[0]<100 and pix[2]<50):
        del name
        return False
      count+=1
    return True
  
  def picIdentify(self, name):
    image=Image.open(name)
    j=0
    k=0
    oxi=0
    oil=0
    while j<128:
      while k<128: 
        pix=image.getpix(j,k)
        if not ((pix[1]>100 and pix[0]<100 and pix[2]<50) or (pix[0]>120 and pix[1]>120 and pix[2]>120)):
          if (pix[0]>130 and pix[1]<200 and pix[1]>70 and pix[2]<125):
            oxi+=1
          else if (pix[1]<60 and pix[0]<60 and pix[2]<60):
            oil+=1
          else:
        k+=1
      k=0
      j+=1
    return self.calculate(oxi,oil)
  
  def calculate(self,oxi,oil):
    perAllOxi=oxi/16384
    perAllOil=oil/16384
    oxiToOil=oxi/oil
    oxiOil=oxi+oil
    perOxi=oxi/oxiOil
    perOil=oil/oxiOil
    return perAllOxi, perAllOil, oxiToOil, perOxi, perOil
  
  
