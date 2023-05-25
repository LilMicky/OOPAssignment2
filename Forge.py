from Workshop import *
from Crafter import *
from Weapon import *

print(type(Crafter))
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
        # Removing materials used to craft the weapon.
        materials[primaryMaterial.__class__.__name__] -= 1
        materials[catalystMaterial.__class__.__name__] -= 1

        damage = Weapon.calculateDamage(self, primaryMaterial, catalystMaterial)

        return Weapon(name, damage, primaryMaterial, catalystMaterial)

    def disassemble(self, weapon, materials):
        """
        Disassembles a weapon and returns the materials.

        Parameters:
            weapon (object) : The weapon.
            materials (list) : The list of materials.

        Returns:
            disassembledWeapon : The disassembled weapon.
        """
        # Returning materials used to craft it
        materials[weapon.primaryMaterial.__class__.__name__] += 1
        materials[weapon.catalystMaterial.__class__.__name__] += 1

        return weapon