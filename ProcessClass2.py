import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image

class ProcessClass:
    
    def pic(self, name):
        #image = cv2.imread(name)
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        
        img = cv2.imread(name,0)
        edges = cv2.Canny(img,100,200)
        
    
        image=Image.open(edges)
        pixel=image.load()
        j=5
        k=54
        count=0
        while j<40:
            while k<74:
                pix=pixel[j,k]
                if pix[0]==255 and pix[1]==255 and pix[2]==255:
                    count+=1
                k+=1
            k=0
            j+=1
        if count<15:
            os.remove(name)
            return False
        
        j=88
        k=54
        count=0
        while j<123:
            while k<74:
                pix=pixel[j,k]
                if pix[0]==255 and pix[1]==255 and pix[2]==255:
                    count+=1
                k+=1
            k=0
            j+=1
        if count<15:
            os.remove(name)
            return False
        else:
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
                if not ((pix[0]<50 and pix[0]>25 and pix[1]<80 and pix[1]>25 and pix[2]<30) or (pix[0]>120 and pix[1]>120 and pix[2]>120)):
                    if (pix[0]>75 and pix[0]<195 and pix[1]<155 and pix[1]>60 and pix[2]<100 and pix[2]>75):
                        oxi+=1
                    if (pix[0]<90 and pix[1]<95 and pix[2]<165):
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
