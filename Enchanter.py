from Crafter import *
from Enchantment import *

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

        return Enchantment(name, magicDamage, primaryMaterial, catalystMaterial)

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
    
    def enchant(self, weaponsList, weaponsToBeEnchanted, enchantmentList):
        """
        Enchants any given weapons.

        Parameters:
            weaponsList (list) : The list of weapons stored in the workshop.
            weaponsToBeEnchanted (string / list) : The string or list of weapon(s) to be enchanted.
            enchantmentList (list) : The list of enchantments stored in the workshop.
        """
        pass