'''
File: Enchantment.py
Description: This files contains the code for the enchantment class.
Author: Harrison Jenkins
Student ID: 110348652
EmailID: jenhi001
This is my own work as defined by the University's Academic Misconduct Policy.
'''


from Workshop import *
from Crafter import *
from Enchanter import *
from Forge import *
from Weapon import *
from Materials import *


class Enchantment():
    """
    A class representing an enchantment for a weapon.

    Attributes
    ----------
    name : string
        the name of the enchantment.
    magicDamage : float
        the magic damage of the enchantment.
    effect : string
        the effect of the enchantment.
    primaryMaterial : string
        the primary material of the enchantment.
    catalystMaterial : string
        the catalyst material of the enchantment.

    Methods
    -------
    calculateMagicDamage()
        calculates the magic damage of the enchantment.
    useEffect()
        uses the effect of the enchantment.

    """
    def __init__(self, name, magicDamage, effect, primaryMaterial, catalystMaterial):

        # Assigning values to private attributes.
        self.__name = name
        self.__magicDamage = magicDamage
        self.__effect = effect
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial

    def calculateMagicDamage(self, primaryMaterial, catalystMaterial):
        """
        Calculates the damage of an enchantment.

        Parameters:
            primaryMaterial (string) : The primary material of the enchantment.
            catalystMaterial (string) : The catalyst material of the enchantment.

        Returns:
            magicDamage (float) : The damage of the enchantment.
                
        """
        return primaryMaterial.magicPower + catalystMaterial.magicPower

    def useEffect(self):
        """
        Uses the enchantment effect and deals the damage associated with the enchantment.

        Returns:
            effectMessage (string) : An effect message stating what enchantment was used and the effect it has.

        """
        return f"{self.name} enchantment and {self.effect}"

    def getName(self):
        """
        Retreives the name of the enchantment.

        Returns:
            name (string) : The name of the enchantment.
        """
        return self.__name

    def getMagicDamage(self):
        """
        Retreives the magic damage associated with the enchantment.

        Returns:
            magicDamage (float) : The magic damage of the enchantment.
        """
        return self.__magicDamage

    def getEffect(self):
        """
        Retrieves the effect associated with the enchantment.

        Returns:
            effect (string) : The effect of the enchantment.
        """
        return self.__effect

    def getPrimaryMaterial(self):
        """
        Retrieves the primary material associated with the enchantment.

        Returns:
            primaryMaterial (string) : The primary material of the enchantment.
        """
        return self.__primaryMaterial

    def getSecondaryMaterial(self):
        """
        Retrieves the catalyst material associated with the enchantment.

        Returns:
            catalystMaterial (string) : The catalyst material of the enchantment.
        """
        return self.__catalystMaterial

    def setName(self, name):
        """
        Sets the name of the enchantment.

        Parameters:
            name (string) : The name of the enchantment.
        """
        self.__name = name

    def setEffect(self, effect):
        """
        Sets the effect of the enchantment.

        Parameters:
            effect (string) : The effect of the enchantment.
        """
        self.__effect = effect

    def setMagicDamage(self, magicDamage):
        """
        Sets the magic damage of the enchantment.

        Parameters:
            magicDamage (float) : the magic damage of the enchantment.
        """
        self.__magicDamage = magicDamage

    # Properties for variables with getters and setters
    name = property(getName, setName)
    magicDamage = property(getMagicDamage, setMagicDamage)
    effect = property(getEffect, setEffect)

    # Properties for variables with just getters
    primaryMaterial = property(getPrimaryMaterial)
    catalystMaterial = property(getSecondaryMaterial)