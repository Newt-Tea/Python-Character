import string
import Weapon
import os
from health_bar import HealthBar

class Character:
    alive: bool = True
    def __init__(self,name:string,health:int,maxHealth:int = 100, weapon:Weapon = Weapon.Fists): 
        self.name=name
        self.health=health
        self.maxHealth=maxHealth
        self.weapon = weapon
        self.dmg=self.weapon.dmg
        
    def attack(self, target) -> None:
        if (target.health >= self.dmg) & (self.health > 0):
            target.health -= self.dmg
            target.health = max(target.health, 0)
            target.health_bar.update()
            print(f"{self.name} dealt {self.dmg} damage to {target.name} with {self.weapon.name}")
        elif target.health <= self.dmg:
            target.alive = False
        else:
            self.alive = False

class Hero(Character):
    def __init__(self,name,health) -> None:
        super().__init__(name=name,health=health)

        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color = "green")

    def equip(self,weapon):
        self.weapon=weapon
        self.dmg=weapon.dmg
        print(f"{self.name} equiped a(n) {weapon.name}")

    def drop(self) -> None:
        print(f"{self.name} dropped their {self.weapon.name}!")
        self.weapon = self.defaultWeapon

class Enemy(Character):
    def __init__(self,name,health) -> None:
        super().__init__(name=name,health=health)

        self.health_bar = HealthBar(self, color = "red")

# Init of default Characters
