import random
class Dragon:
  def __init__ (self,name):
    self.anger=100
    self.name=name
    self.pos=0
    self.power=random.randint(1,5)
    print("Dragon "+self.name+" spawned with "+str(self.power)+" power")
  
  def getPosition(self)  :
    return self.pos
  
  def getPower(self):
    return self.power
    
  def roar(self, loudness):
    if loudness > 100:
      print("ROAAAR!!!!")
    else:
      print("--squeak--")
  
  def fly(self, distance) :
    self.pos = self.pos+distance

  def fight(self,anotherdragon):
    if self.getPower()>anotherdragon.getPower():
      print(self.name + " wins!!!")
    else:
     print(anotherdragon.name + " wins!!!")
  

alan = Dragon("Alan Turing")
ada = Dragon("Ada Lovelace")
tim = Dragon("Tim Berners Lee")
steve = Dragon("Steve Jobs")

alan.fly(100)
print(alan.getPosition())
alan.fly(200)
print(alan.getPosition())

alan.roar(10)
alan.roar(1000)
