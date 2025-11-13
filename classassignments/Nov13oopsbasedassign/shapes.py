import math
# select cylinder
class Cylinder:
  def __init__(self,radius,height):
    self.r=radius
    self.h=height
  def calculateCSA(self):
    return 2*math.pi*self.r*self.h 
  def calculateTSA(self):
    return 2*math.pi*self.r*(self.r+self.h)
  def calculateVolume(self):
    return math.pi*self.r**2*self.h

# select cone
class Cone:
  def __init__(self,radius,height):
    self.r=radius
    self.h=height
    self.l=math.sqrt(self.r**2+self.h**2)
  def calculateCSA(self):
    return math.pi*self.r*self.l 
  def calculateTSA(self):
    return math.pi*self.r*(self.r+self.l)
  def calculateVolume(self):
    return (1/3)*math.pi*self.r**2*self.h   

# select cube
class Cube:
  def __init__(self,side):
    self.a=side
  def calculateCSA(self):
    return 4*self.a**2 
  def calculateTSA(self):
    return 6*self.a**2
  def calculateVolume(self):
    return self.a**3

# select cuboid
class Cuboid:
  def __init__(self,length,breadth,height):
    self.l=length
    self.b=breadth
    self.h=height
  def calculateCSA(self):
    return 2*self.h*(self.l+self.b) 
  def calculateTSA(self):
    return 2*(self.l*self.b+self.b*self.h+self.h*self.l)
  def calculateVolume(self):
    return self.l*self.b*self.h   

# select Sphere
class Sphere:
  def __init__(self,radius):
    self.r=radius
  def calculateCSA(self):
    return 4*math.pi*self.r**2 
  def calculateTSA(self):
    return 4*math.pi*self.r**2
  def calculateVolume(self):
    return (4/3)*math.pi*self.r**3  