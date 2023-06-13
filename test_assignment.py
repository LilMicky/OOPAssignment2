import unittest

from main import *

## USING MAIN CODE TO CREATE A TEST ENVIRONMENT ##
# Creating a workshop, forge, enchanter.
workshop = Workshop(Forge(), Enchanter())

# Create a set of materials and lists for testing.
materials = [Maple(), Oak(), Ash(), Bronze(), Iron(), Steel(),
Ruby(), Sapphire(), Emerald(), Diamond(), Amethyst(), Onyx()]

weaponBlueprints = {
"Sword": [Steel(), Maple()],
"Shield": [Bronze(), Oak()],
"Axe": [Iron(), Ash()],
69: [Steel(), Ash()],
"Bow": [Oak(), Maple()],
"Wand": [Ash(), Oak()],
"Staff": [Bronze(), Maple()],
"Dagger": [Bronze(), Bronze()]}

enchantmentBlueprints = {
"Holy": [Diamond(), Diamond()],
"Lava": [Ruby(), Onyx()],
"Pyro": [Ruby(), Diamond()],
"Darkness": [Onyx(), Amethyst()],
"Cursed": [Onyx(), Onyx()],
"Hydro": [Sapphire(), Emerald()],
"Venomous": [Emerald(), Amethyst()],
"Earthly": [Emerald(), Emerald()]}

enchantedWeapons = ["Holy Greatsword", "Molten Defender", "Berserker Axe", "Soul Eater",
"Twisted Bow", "Wand of the Deep", "Venemous Battlestaff"]

# Adds a number of materials to use for crafting.
for material in materials:
    if isinstance(material, Wood):
        workshop.addMaterial(material.__class__.__name__, 20)
    elif isinstance(material, Metal):
        workshop.addMaterial(material.__class__.__name__, 10)
    else:
        workshop.addMaterial(material.__class__.__name__, 5)

class TestAssignment(unittest.TestCase):
    def testWeapon(self):
        #calcDmg
        #atk
        #assert raises - mismatached inputs
        #assert equals - values of dmg
        pass

    def testEnchanment(self):
        #calcMagicDmg
        #useEffect
        pass

    def testForgeAndWeapon(self):

        # Craft, Calculate Damage, and Attack method being tested for each weapon
        for weapon, materials in weaponBlueprints.items():
            craftedWeapon = workshop.forge.craft(weapon, materials[0], materials[1], workshop.materials)
            self.assertEqual(craftedWeapon.__class__.__name__, "Weapon")
            self.assertEqual(craftedWeapon.damage, Weapon.calculateDamage(self, materials[0], materials[1]))
            self.assertEqual(craftedWeapon.attack(), f"It deals {Weapon.calculateDamage(self, materials[0], materials[1]):.2f} damage.")


        #disassemble

    def testEnchanter(self):
        #craft
        #disassemble
        #enchant
        pass

    def testWorkshop(self):
        #addWeapon
        #addEnchantment
        #addMaterial
        #removeWeapon
        #removeEnchantment
        #removeMaterial
        #displayWeapons
        #displayEnchantments
        #displayMaterials
        pass


unittest.main()

