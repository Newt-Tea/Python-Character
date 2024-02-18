import string
import Weapon
import os
from health_bar import HealthBar

class Character:
    """
    A Class used to represent a Character

    ...

    Attributes
    ----------
    __alive__ : bool
        Determines if the character is alive or not
    __default_weapon__ : weapon
        Sets the default weapon for the character
    name : string
        The name of the character
    health : int, optional
        The current health of the character `100` (default 100)
    maxHealth: int, optional
        The max health of the character `100` (default 100)
    weapon : Weapon, optional
        The currently equipped weapon of the character `Fists` (default Fists)

    Methods
    -------
    attack(self, target)
        Attacks the target character
    """
    alive : bool = True
    __default_weapon__ : Weapon = Weapon.Fists

    def __init__(self,name:string,health:int = 100,maxHealth:int = 100, weapon:Weapon = Weapon.Fists) -> None: 
        self.name=name
        self.health=health
        self.maxHealth=maxHealth
        self.weapon = weapon
        self.__dmg__ = weapon.dmg

    @property
    def dmg(self):
        return self.__dmg__
    
        
    def attack(self, target) -> None:
        """Attacks other Characters"""
        # Checking if anyone has died
        if (target.health >= self.__dmg__) & (self.health > 0):
            target.health -= self.__dmg__
            #Prevents health dropping below 0
            target.health = max(target.health, 0)
            target.health_bar.update()
            print(f"{self.name} dealt {self.__dmg__} damage to {target.name} with {self.weapon.name}")

        #Check if target is alive
        elif target.health <= self.__dmg__:
            target.__alive__ = False

        #Check if you are alive
        else:
            self.__alive__ = False

#Inherited from parent Character
#Default player character
class Hero(Character):
    """
    A class to create the player character
    
    ...
    
    Attributes
    ----------
    name : str, optional
        sets the name of the hero (default Hero)
    health : int, optional
        sets the health of the hero (default 100)

    
    
    Methods
    -------
    equip(weapon)
        Equips a weapon to the hero
    drop
        Drops the currently equipped weapon
    """    
    def __init__(self,name:string = "Hero",health:int = 100) -> None:
        super().__init__(name=name,health=health)

        self.health_bar = HealthBar(self, color = "green")

    def equip(self,weapon:Weapon) -> None:
        """
        Equips a weapon to the hero
        """
        
        self.weapon=weapon
        self.__dmg__=weapon.dmg

        print(f"{self.name} equiped a(n) {weapon.name}")

    def drop(self) -> None:
        """Drops the currently equipped weapon"""
        print(f"{self.name} dropped their {self.weapon.name}!")
        self.weapon = self.__default_weapon__

#Inherited from parent Character
# Default enemy character
class Enemy(Character):
    """
    A class to create an enemy character
    
    ...
    
    Attributes
    ----------
    name : str, optional
        sets the name of the enemy (default Enemy)
    health : int, optional
        sets the health of the enemy (default 100)
    """
    def __init__(self,name:string = "Enemy",health:int = 100) -> None:
        super().__init__(name=name,health=health)

        self.health_bar = HealthBar(self, color = "red")
