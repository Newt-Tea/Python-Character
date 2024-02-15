import Character
from Character import Weapon


Fists = Weapon.Weapon("Fists",3)
Mace = Weapon.Weapon("Mace",5)
ShortBow = Weapon.Weapon("Short Bow",4)

Hero = Character.Character("Hero",100,100,Fists)
Enemy = Character.Character("Enemy",100,100,Fists)
Hero.equip(Mace)

while(True):
    Hero.attack(Enemy)
    