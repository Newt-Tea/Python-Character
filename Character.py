
import string
import Weapon
import os
import time

class Character:

    weapon=Weapon.Fists
    alive = True

    def __init__(self,name:string,health:int,maxHealth:int,): 
        self.name=name
        self.health=health
        self.maxHealth=maxHealth
        self.dmg=self.weapon.dmg

    def attack(self, target) -> None:
        while((target.alive==True) & (self.alive==True)):

            if(target.health > 0):

                print(f"You: {self.health}/{self.maxHealth} Enemy: {target.health}/{target.maxHealth}")

                target.health-=self.dmg
                print (f"{self.name} attacks {target.name} for {self.dmg} health")

                self.health-=target.dmg
                print (f"{target.name} attacks {self.name} for {target.dmg} health")

                time.sleep(0.4)
                os.system('cls')
            else:
                print(f"You: {self.health}/{self.maxHealth} Enemy: {target.health}/{target.maxHealth}")
                target.alive = False
                print(f"{target.name} was killed by {self.name}")
                time.sleep(3)

    def equip(self,weapon):
        self.dmg=weapon.dmg
        self.weapon=weapon
        print(f"{self.name} equiped {weapon.name}")
    
    def healthBar(self,target):
        while((self.alive==True) & (target.alive == True)):
            print(f"You: {self.health}/{self.maxHealth} Enemy: {target.health}/{target.maxHealth}")

# Init of default Characters
Hero = Character