import Character
from Character import Weapon

# Initialization of Character objects
Hero = Character.Hero
Enemy = Character.Enemy
Hero.equip(Weapon.Mace)

Hero.attack(Enemy)