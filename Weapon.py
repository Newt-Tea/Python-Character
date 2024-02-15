import string
class Weapon:
    def __init__(self,name:string,dmg:int,speed:int):
        self.name=name
        self.dmg=dmg
        self.speed=speed
        secs = speed*0.6

Fists = Weapon("Fists",3,5)
Mace = Weapon("Mace",5,3)
ShortBow = Weapon("Short Bow",4,4)
