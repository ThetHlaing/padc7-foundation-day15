class Animal:
    def __init__(self,name):
        self.name = name
        self._leg = None

    def speak(self):
        print(self.name,"Speaking")

    def getLeg(self):
        if self._leg is None:
            return 4
        else:
            return self._leg

    def setLeg(self,value):
        self._leg = value
    
    # deleting the values 
    def delLeg(self): 
        del self._leg 

    leg = property(getLeg,setLeg)


animal = Animal("Breakie")

animal.speak()
animal.leg = 5
print(animal.leg)