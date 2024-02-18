from Character import Hero,Enemy
from Character import Weapon
import os

# Initialization of Character objects
hero = Hero("Hero",100)
enemy = Enemy("Enemy",100)
hero.equip(Weapon.Mace)
def run() -> None :
    """Runs the battle sim"""
    while (hero.alive & enemy.alive) == True:
        os.system("cls")
        hero.attack(enemy)
        enemy.attack(hero)
        hero.health_bar.draw()
        enemy.health_bar.draw()

        input()
    if hero.alive == False:
            print(f"{hero.name} killed {enemy.name} with {hero.weapon.name}")
    else:
         print(f"{hero.name} killed {enemy.name} with {hero.weapon.name}")
run.__doc__ = "Runs the battle sim"

run()