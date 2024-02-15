import Character
from Character import Weapon

# Initialization of Character objects
Hero = Character.Character("Hero",100,100,Weapon.Fists)
Enemy = Character.Character("Enemy",100,100,Weapon.Fists)
Hero.equip(Weapon.Mace)

while(Hero.attack(Enemy)==True):
    break