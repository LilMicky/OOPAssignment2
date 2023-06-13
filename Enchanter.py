'''
File: Enchanter.py
Description: This files contains the code for the enchanter class.
Author: Harrison Jenkins
Student ID: 110348652
EmailID: jenhi001
This is my own work as defined by the University's Academic Misconduct Policy.
'''


from Workshop import *
from Crafter import *
from Forge import *
from Weapon import *
from Enchantment import *
from Materials import *


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
        materials[primaryMaterial.__class__.__name__] -= 1
        materials[catalystMaterial.__class__.__name__] -= 1 

        magicDamage = Enchantment.calculateMagicDamage(self, primaryMaterial, catalystMaterial)
        
        # Empty variable to assign effect to.
        effect = ""

        # Finding effect for the enchantment
        for enchant in self.recipes.keys():
            if name == enchant:
                effect = self.recipes[name]

        return Enchantment(name, magicDamage, effect, primaryMaterial, catalystMaterial)

    def disassemble(self, enchantment, materials):
        """
        Disassembles an enchantment and returns the materials.

        Parameters:
            enchantment (object) : The enchantment.
            materials (list) : The list of materials.

        Returns:
            disassembledEnchantment: The disassembled materials.
        """

        materials[enchantment.primaryMaterial.__class__.__name__] += 1
        materials[enchantment.catalystMaterial.__class__.__name__] += 1 
        
        return enchantment
    
    def enchant(self, weapon, enchantName, enchantment):
        """
        Enchants any given weapons.

        Parameters:
            weapon (string) : The list of weapons stored in the workshop.
            enchantmentName (string) : The new name of the enchanted weapon.
            enchantment (string) : The enchantment to be applied.
        """
        weapon.name = enchantName
        weapon.enchantment = enchantment
        weapon.damage *= enchantment.magicDamage
      
                

