'''
File: Weapon.py
Description: This files contains the code for the weapon class.
Author: Harrison Jenkins
Student ID: 110348652
EmailID: jenhi001
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from Workshop import *
from Crafter import *
from Enchanter import *
from Forge import *
from Enchantment import *
from Materials import *


class Weapon():
    """
    A class representing a weapon.

    Attributes
    ----------
    name : string
        name of the weapon.

    damage : float
        damage of the weapon.

    primaryMaterial : string
        primary material of the weapon.

    catalystMaterial : string
        catalyst material of the weapon.

    enchantment : string
        the enchantment attached to the weapon.
    
    enchanted : boolean
        the status of whether the weapon is enchanted.

    Methods
    -------
    calculateDamage()
        Calculates the damage of a weapon.

    attack()
        Deals attack damage.
    """
    def __init__(self, name, damage, primaryMaterial, catalystMaterial):
        """
        Creates a weapon object.

        Parameters:
            name (string) : The name of the weapon.
            damage (float) : The damage of the weapon.
            primaryMaterial (string) : The primary material of the weapon.
            catalystMaterial (string) : The catalyst material of the weapon.
        """
        # Assigning values to private variables.
        self.__name = name
        self.__damage = damage
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial
        self.__enchantment = ""

    def calculateDamage(self, primaryMaterial, catalystMaterial):
        """
        Calculates the damage of the weapon.

        Returns:
            damage (float) : The damage output.
        """
        if isinstance(primaryMaterial, Wood) and isinstance(catalystMaterial, Wood):
            return primaryMaterial.strength * catalystMaterial.strength
        elif isinstance(primaryMaterial, Metal) and isinstance(catalystMaterial, Metal):
            return (primaryMaterial.strength * primaryMaterial.purity) + (catalystMaterial.strength * catalystMaterial.purity)
        elif isinstance(primaryMaterial, Wood) and isinstance(catalystMaterial, Metal):
            return primaryMaterial.strength * (catalystMaterial.strength * catalystMaterial.purity)
        
        # In case of the primary material being metal and catalyst being wood.
        else:
            return (primaryMaterial.strength * primaryMaterial.purity) * catalystMaterial.strength
            
    def attack(self):
        """
        Attacks and deals the damage associated with the weapon.

        Returns:
            attackMessage (string) : An attack message displaying the damage output.
        """
        return f"It deals {self.damage:0.2f} damage."

    def getName(self):
        """
        Retreives the name of the weapon.

        Returns:
            name (string) : The name of the weapon.
        """
        return self.__name

    def getDamage(self):
        """
        Retreives the damage of the weapon.

        Returns:
            damage (float) : The damage of the weapon.
        """
        return self.__damage

    def getEnchanted(self):
        """
        Retreives the enchanted status of the weapon.

        Returns:
            enchanted (boolean) : The enchanted status of the weapon.
        """
        return self.__enchanted

    def getPrimaryMaterial(self):
        """
        Retreives the primary material of the weapon.

        Returns:
            primaryMaterial (string) : The primary material of the weapon.
        """
        return self.__primaryMaterial

    def getSecondaryMaterial(self):
        """
        Retreives the catalyst material of the weapon.

        Returns:
            catalystMaterial (string) : The catalyst material of the weapon.
        """
        return self.__catalystMaterial

    def getEnchantment(self):
        """
        Retreives the enchantment of the weapon.

        Returns:
            enchanment (string) : The enchantment of the weapon.
        """
        return self.__enchantment

    def setName(self, name):
        """
        Sets the name of the weapon.

        Parameters:
            name (string) : The name of the weapon.
        """
        self.__name = name

    def setDamage(self, damage):
        """
        Sets the damage of the weapon.

        Parameters:
            damage (float) : The damage of the weapon.
        """
        self.__damage = damage

    def setEnchanted(self, enchanted):
        """
        Sets the enchanted status of the weapon.

        Parameters:
            enchanted (boolean) : The enchanted status of the weapon.
        """
        self.__enchanted = enchanted

    def setEnchantment(self, enchantment):
        """
        Sets the enchantment of the weapon.

        Parameters:
            enchantment (string) : The enchantment of the weapon.
        """
        self.__enchantment = enchantment

    # Properties for variables with getters and setters
    name = property(getName, setName)
    damage = property(getDamage, setDamage)
    enchanted = property(getEnchanted, setEnchanted)
    enchantment = property(getEnchantment, setEnchantment)

    # Properties for variables with just getters
    primaryMaterial = property(getPrimaryMaterial)
    catalystMaterial = property(getSecondaryMaterial)