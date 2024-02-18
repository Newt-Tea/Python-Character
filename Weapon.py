import string
class Weapon:
    """
    A class to create weapon objects for characters
    
    ...
    
    Attributes
    ----------
    name : str
        The name of the weapon
    dmg : str
        The amount of damage the weapon does
    speed : int (currently not in use)
        How often the weapon attacks
    """
    
    def __init__(self,name:string,dmg:int,speed:int) -> None:
        """
        Parameters
        ----------
        name : str
            The name of the weapon
        dmg : int
            The amount of damage the weapon does
        speed : int
            How often the weapon attacks
        """
        
        self.name=name
        self.dmg=dmg
        #self.speed=speed
        #secs = speed*0.6


# Creation of default objects
Fists = Weapon("Fists",3,5)
Mace = Weapon("Mace",5,3)
ShortBow = Weapon("Short Bow",4,4)
