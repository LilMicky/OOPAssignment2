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


