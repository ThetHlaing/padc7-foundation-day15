# The main work of decorators is they are used to add functionality to the existing code. 
# Also called metaprogramming, as a part of the program tries to modify another part of the program at compile time.

class Animal:
    def __init__(self,name):
        self.name = name
        self._leg = None

    def speak(self):
        print(self.name,"Speaking")

    @property
    def leg(self):
        if self._leg is None:
            return 4
        else:
            return self._leg

    @leg.setter
    def leg(self,value):
        self._leg = value
    
    @leg.deleter
    def leg(self): 
        del self._leg 


animal = Animal("Breakie")

animal.speak()
animal.leg = 5
print(animal.leg)