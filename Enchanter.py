from Crafter import *

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