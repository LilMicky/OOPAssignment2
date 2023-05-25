'''
File: Main.py
Description: This files contains the main code for the assignment.
Author: Harrison Jenkins
Student ID: 110348652
EmailID: jenhi001
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import Materials
from abc import ABC, abstractmethod


class Workshop():
    """
    The main class where the enchanter, and forge class objects will be stored. As well as the weapons, enchantments, and materials.

    Attributes
    ----------
    forgeClass : Class
        The class used to forge weapons.

    enchanterClass: Class
        The class used to enchant weapons.

    Methods
    -------
    displayWeapons() :
        Returns a list of weapons stored in the workshop.

    displayEnchantments() :
        Returns a list of enchantments stored in the workshop.

    displayMaterials() :
        Returns a list of materials stored in the workshop.
    """
    def __init__(self, forgeClass, enchanterClass):
        pass

    def displayWeapons(self):
        """
        Returns a list of weapons stored in the workshop.

        Returns:
        Weapons (list): The list of weapons.
        """
        pass

    def displayEnchantments(self):
        """
        Returns a list of enchantments stored in the workshop.

        Returns:
        Enchantments (list): The list of enchantments.
        """
        pass

    def displayMaterials(self):
        """
        Returns a list of materials stored in the workshop.

        Materials (list): The list of materials.
        """
        pass


class Crafter(ABC):
    """
    An abstract class for classes to inherit from.

    Methods
    --------
    craft():
        Does not return anything.
    
    disassemble():
        Does not return anything.
    """
    @abstractmethod
    def craft(self):
        """
        This method will be overidden for creating a weapon.
        """
        pass

    @abstractmethod
    def disassemble(self):
        """
        This method will be overidden for disassembling a weapon.
        """
        pass

class Forge(Crafter):
    """
    This class is a type of Crafter.

    Methods
    --------
    craft(name, primaryMaterial, secondaryMaterial, materials):
        Returns a weapon.

    disassemble(weapon , materials):
        Returns the materials from a disassembled weapon.
    """
    def craft(self, name, primaryMaterial, catalystMaterial, materials):
        """
        Crafts and returns a weapon.

        Parameters:
            name (string) : The name of the weapon.
            primaryMaterial (string) : The primary material.
            catalystMaterial (string) : The catalyst material.
            materials (list) : The list of materials.

        Returns:
            weapon (object) : The weapon object.
        """
        pass

    def disassemble(self, weapon, materials):
        """
        Disassembles a weapon and returns the materials.

        Parameters:
            weapon (object) : The weapon.
            materials (list) : The list of materials.

        Returns:
            disassembledWeapon : The disassembled materials.
        """
        pass

class Enchanter(Crafter):
    def __init__(self):
        self.recipes = {
            "Holy": "pulses a blinding beam of light",
            "Lava": "melts the armour off an enemy",
            "Pyro": "applies a devastating burning effect",
            "Darkness": "binds the enemy in dark vines",
            "Cursed": "causes the enemy to become crazed",
            "Hydro": "envelops the enemy in a suffocating bubble",
            "Venomous": "afflicts a deadly, fast-acting toxin"}
        
    def craft(self, name, primaryMaterial, catalystMaterial, materials):
        """
        Crafts and returns an enchantment.

        Parameters:
            name (string) : The name of the enchantment.
            primaryMaterial (string) : The primary material.
            catalystMaterial (string) : The catalyst material.
            materials (list) : The list of materials.
                
        Returns:
            enchantment (object) : The enchantment object.    
        """
        pass

    def disassemble(self, enchantment, materials):
        """
        Disassembles an enchantment and returns the materials.

        Parameters:
            enchantment (object) : The enchantment.
            materials (list) : The list of materials.

        Returns:
            disassembledEnchantment: The disassembled materials.
        """
        pass

    def enchant(self, weaponsList, weaponsToBeEnchanted, enchantmentList):
        """
        Enchants any given weapons.

        Parameters:
            weaponsList (list) : The list of weapons stored in the workshop.
            weaponsToBeEnchanted (string / list) : The string or list of weapon(s) to be enchanted.
            enchantmentList (list) : The list of enchantments stored in the workshop.
        """
        pass

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

        Returns:
            weapon (object) : A weapon object.
        """
        # Assigning values to private variables.
        self.__name = name
        self.__damage = damage
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial
        self.__enchantment = ""
        self.__enchanted = False

    def calculateDamage(self):
        """
        Calculates the damage of the weapon.

        Returns:
            damage (float) : The damage output.
        """
        pass

    def attack(self):
        """
        Attacks and deals the damage associated with the weapon.

        Returns:
            attackMessage (string) : An attack message displaying the damage output.
        """
        pass

    def getName(self):
        """
        Retreives the name of the weapon.

        Returns:
            name (string) : The name of the weapon.
        """
        pass

    def getDamage(self):
        """
        Retreives the damage of the weapon.

        Returns:
            damage (float) : The damage of the weapon.
        """
        pass

    def getEnchanted(self):
        """
        Retreives the enchanted status of the weapon.

        Returns:
            enchanted (boolean) : The enchanted status of the weapon.
        """
        pass

    def getPrimaryMaterial(self):
        """
        Retreives the primary material of the weapon.

        Returns:
            primaryMaterial (string) : The primary material of the weapon.
        """
        pass

    def getSecondaryMaterial(self):
        """
        Retreives the catalyst material of the weapon.

        Returns:
            catalystMaterial (string) : The catalyst material of the weapon.
        """
        pass

    def getEnchantment(self):
        """
        Retreives the enchantment of the weapon.

        Returns:
            enchanment (string) : The enchantment of the weapon.
        """
        pass

    def setName(self, name):
        """
        Sets the name of the weapon.

        Parameters:
            name (string) : The name of the weapon.
        """
        pass

    def setDamage(self, damage):
        """
        Sets the damage of the weapon.

        Parameters:
            damage (float) : The damage of the weapon.
        """
        pass

    def setEnchanted(self, enchanted):
        """
        Sets the enchanted status of the weapon.

        Parameters:
            enchanted (boolean) : The enchanted status of the weapon.
        """
        pass

    def setEnchantment(self, enchantment):
        """
        Sets the enchantment of the weapon.

        Parameters:
            enchantment (string) : The enchantment of the weapon.
        """
        pass

    # Properties for variables with getters and setters
    name = property(getName, setName)
    damage = property(getDamage, setDamage)
    enchanted = property(getEnchanted, setEnchanted)
    enchantment = property(getEnchantment, setEnchantment)

    # Properties for variables with just getters
    primaryMaterial = property(getPrimaryMaterial)
    catalystMaterial = property(getSecondaryMaterial)

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

    def calculateMagicDamage(self):
        """
        Calculates the damage of an enchantment.

        Returns:
            magicDamage (float) : The damage of the enchantment.
                
        """
        pass

    def useEffect(self):
        """
        Uses the enchantment effect and deals the damage associated with the enchantment.

        Returns:
            effectMessage (string) : An effect message stating what enchantment was used and the effect it has.

        """

    def getName(self):
        """
        Retreives the name of the enchantment.

        Returns:
            name (string) : The name of the enchantment.
        """
        pass

    def getMagicDamage(self):
        """
        Retreives the magic damage associated with the enchantment.

        Returns:
            magicDamage (float) : The magic damage of the enchantment.
        """
        pass

    def getEffect(self):
        """
        Retrieves the effect associated with the enchantment.

        Returns:
            effect (string) : The effect of the enchantment.
        """
        pass

    def getPrimaryMaterial(self):
        """
        Retrieves the primary material associated with the enchantment.

        Returns:
            primaryMaterial (string) : The primary material of the enchantment.
        """
        pass

    def getSecondaryMaterial(self):
        """
        Retrieves the catalyst material associated with the enchantment.

        Returns:
            catalystMaterial (string) : The catalyst material of the enchantment.
        """
        pass

    def setName(self, name):
        """
        Sets the name of the enchantment.

        Parameters:
            name (string) : The name of the enchantment.
        """
        pass

    def setEffect(self, effect):
        """
        Sets the effect of the enchantment.

        Parameters:
            effect (string) : The effect of the enchantment.
        """
        pass

    def setMagicDamage(self, magicDamage):
        """
        Sets the magic damage of the enchantment.

        Parameters:
            magicDamage (float) : the magic damage of the enchantment.
        """
        pass

    # Properties for variables with getters and setters
    name = property(getName, setName)
    magicDamage = property(getMagicDamage, setMagicDamage)
    effect = property(getEffect, setEffect)

    # Properties for variables with just getters
    primaryMaterial = property(getPrimaryMaterial)
    catalystMaterial = property(getSecondaryMaterial)




