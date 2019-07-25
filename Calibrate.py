
class Calibrate:
  
  def storage(self, odom, tim, im):
    if im==1:
      self.image1=(odom, tim)
    elif im==2:
      self.image2=(odom, tim)
    elif im==3:
      self.image3=(odom, tim)
    elif im==4:
      self.image4=(odom, tim)
    else:
      self.image5=(odom, tim)
      
  def reset(self):
    self.image1=(0,0)
    self.image2=(0,0)
    self.image3=(0,0)
    self.image4=(0,0)
    self.image5=(0,0)

  def calGreen(self):
    
  
  def calOrange(self):
    
  
  def calBlack(self):
    
    
