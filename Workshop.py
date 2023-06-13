'''
File: Workshop.py
Description: This files contains the code for the workshop class.
Author: Harrison Jenkins
Student ID: 110348652
EmailID: jenhi001
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from abc import ABC, abstractmethod
from Crafter import *
from Enchanter import *
from Forge import *
from Weapon import *
from Enchantment import *
from Materials import *


class antiDuplication():
    
    def display(self, list):

        # String to add each msg to then return
        emptyString = ""

        # Only materials are in a dict so if this is true, it has to be materials.
        if list.__class__.__name__ == "dict":
            for material in list:
                emptyString += f"{material}: {list[material]} remaining.\n"

            return emptyString
        
        if list.__class__.__name__ == "Weapon":
            for weapon in list:
                if weapon.enchantment == "":
                    emptyString += f"The {weapon.name} is not enchanted. {weapon.attack()}\n"
                else:
                    emptyString += f"The {weapon.name} is imbued with a {weapon.enchantment.useEffect()}. {weapon.attack()}\n"

            return emptyString
        
        for enchant in list:
                emptyString += f"A {enchant.name} enchantment is stored in the workshop.\n"

        return emptyString
    
                

class Workshop(antiDuplication):
    """
    The main class where the enchanter, and forge class objects will be stored. As well as the weapons, enchantments, and materials.

    Attributes
    ----------
    forge : class
        The class used to forge weapons.

    enchanter : class
        The class used to enchant weapons.

    weapons : list
        A list containing all of the weapons created.

    enchantments : list
        A list containing all of the enchantments created.
    
    materials : list
        A list containing all of the materials created.
    
    Methods
    -------
    addWeapon() :
        Adds a weapon to the workshop.

    addEnchantment() :
        Adds an enchantment to the workshop.

    addMaterial() :
        Adds a material to the workshop.

    removeWeapon() :
        Removes a weapon from the workshop.

    removeEnchantment() :
        Removes an enchantment from the workshop.

    removeMaterial() :
        Remove an enchantment from the workshop.
    
    displayWeapons() :
        Returns a list of weapons stored in the workshop.

    displayEnchantments() :
        Returns a list of enchantments stored in the workshop.

    displayMaterials() :
        Returns a list of materials stored in the workshop.
    """
    def __init__(self, forgeClass, enchanterClass):
        self.forge = forgeClass
        self.enchanter = enchanterClass
        self.weapons = []
        self.enchantments = []
        self.materials = {"Maple": 0, "Oak": 0, "Ash": 0, "Bronze": 0, "Iron": 0, "Steel": 0,
        "Ruby": 0, "Sapphire": 0, "Emerald": 0, "Diamond": 0, "Amethyst": 0, "Onyx": 0}

    def addWeapon(self, weapon):
        """
        Adds a new weapon to the workshop.

        Parameters:
            weapon (object) : The weapon object being added.
        """
        self.weapons.append(weapon)

    def addEnchantment(self, enchantment):
        """
        Adds a new enchantment to the workshop.

        Parameters:
            enchantment (object) : The enchantment object being added.
        """
        self.enchantments.append(enchantment)

    def addMaterial(self, material, total):
        """
        Adds new materials to the workshop.

        Parameters:
            materials (object) : The materials object being added.
            total (int) : The amount of materials being added.
        """
        self.materials[material] = total

    def removeWeapon(self, weapon):
        """
        Removes a weapon from the workshop.

        Parameters:
            weapon (object) : The weapon object being removed.
        """
        self.weapons.remove(weapon)

    def removeEnchantment(self, enchantment):
        """
        Removes an enchantment from the workshop.

        Parameters:
            enchantment (object) : The enchantment object being removed.
        """
        self.enchantments.remove(enchantment)

    def removeMaterial(self, material, total):
        """
        Removes materials from the workshop.

        Parameters:
            materials (object) : The materials object being removed.
            total (int) : The amount of materials being removed.
        """
        self.materials[material] -= total
    
    def displayWeapons(self):
        """
        Returns a list of weapons stored in the workshop.

        Returns:
        Weapons (list): The list of weapons.
        """
        return super().display(self.weapons)
                

    def displayEnchantments(self):
        """
        Returns a list of enchantments stored in the workshop.

        Returns:
        Enchantments (list): The list of enchantments.
        """
        return super().display(self.enchantments)


    def displayMaterials(self):
        """
        Returns a list of materials stored in the workshop.

        Materials (list): The list of materials.
        """
        return super().display(self.materials)
