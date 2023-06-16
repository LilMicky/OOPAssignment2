'''
File: Test_Assignment.py
Description: This files contains the testing code for the main code.
Author: Harrison Jenkins
Student ID: 110348652
EmailID: jenhi001
This is my own work as defined by the University's Academic Misconduct Policy.
'''
import unittest

from Main import *

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
"Scythe": [Steel(), Ash()],
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

for weapon, materials in weaponBlueprints.items():
            craftedWeapon = workshop.forge.craft(weapon, materials[0], materials[1], workshop.materials)
            workshop.addWeapon(craftedWeapon)

for enchantment, materials in enchantmentBlueprints.items():
            craftedEnchantment = workshop.enchanter.craft(enchantment, materials[0], materials[1], workshop.materials)
            workshop.addEnchantment(craftedEnchantment)

class TestAssignment(unittest.TestCase):
    def testForgeCraft(self):
        '''This function tests the Forge's craft method, addWeapon method and removeWeapon method.'''
        newWeapon = workshop.forge.craft("Test Sword", Steel(), Maple(), workshop.materials)
        workshop.addWeapon(newWeapon)

        # Checking if instance of Weapon.
        self.assertEqual(workshop.weapons[-1].__class__.__name__, "Weapon")

        # Checking if it is the correct weapon.
        self.assertEqual(workshop.weapons[-1].name, "Test Sword")

        workshop.removeWeapon(newWeapon)

        # Checking if removed
        self.assertNotEqual(workshop.weapons[-1].name, "Test Sword")

    
    def testCalcDmg(self):
        '''This function tests the calculate damage method.'''
        self.assertEqual(workshop.weapons[0].damage, 90.00)
    
    def testAttack(self):
        '''This function tests the attack method.'''
        self.assertEqual(workshop.weapons[0].attack(), "It deals 90.00 damage.")

    def testForgeDisassemble(self):
        '''This function tests the Forge's disassemble method and addMaterial method.'''

        # Checking length of list and amount of materials before disassembling.
        self.assertEqual(len(workshop.weapons), 8)
        self.assertEqual(workshop.materials["Bronze"], 6)

        workshop.removeWeapon(workshop.forge.disassemble(workshop.weapons[7], workshop.materials))

        # Checking the length of list and amount of materials after disassembling.
        self.assertEqual(workshop.materials["Bronze"], 8)
        self.assertNotEqual(len(workshop.weapons), 8)

    def testEnchant(self):
        '''This function tests the Enchanter's craft method, addEnchantment method, and removeEnchantment method.'''
        newEnchant = workshop.enchanter.craft("Test Enchant", Diamond(), Diamond(), workshop.materials)
        workshop.addEnchantment(newEnchant)

        # Checking if instance of Enchantment.
        self.assertEqual(workshop.enchantments[-1].__class__.__name__, "Enchantment")

        # Checking if it is the correct enchant.
        self.assertEqual(workshop.enchantments[-1].name, "Test Enchant")

        workshop.removeEnchantment(newEnchant)
        workshop.materials["Diamond"] += 2

        # Checking if removed
        self.assertNotEqual(workshop.enchantments[-1].name, "Test Enchant")
        
    def testUseEffect(self):
        '''This function tests the useEffect method.'''
        self.assertEqual(workshop.enchantments[0].useEffect(), "Holy enchantment and pulses a blinding beam of light")

    def testCalcMagicDmg(self):
        '''This function tests the calcMagicDmg method.'''
        self.assertEqual(workshop.enchantments[0].magicDamage, 9.24)

    def testEnchanterDisassemble(self):
        '''This function tests the Enchanter's disassemble method.'''

        # Checking the length of list and amount of materials after disassembling.
        self.assertEqual(len(workshop.enchantments), 8)
        self.assertEqual(workshop.materials["Emerald"], 1)

        workshop.removeEnchantment(workshop.enchanter.disassemble(workshop.enchantments[7], workshop.materials))

        # Checking the length of list and amount of materials after disassembling.
        self.assertEqual(workshop.materials["Emerald"], 3)
        self.assertNotEqual(len(workshop.enchantments), 8)

    def testRemoveMaterial(self):
        '''This function tests the removeMaterial method.'''

        # Check to make sure each material has a value greater than 0.
        for material in workshop.materials:
             self.assertGreater(workshop.materials[material], 0)

        # For each material in workshop.materials I will be removing 1 material until it hits 0.
        for material in workshop.materials:
            while workshop.materials[material] > 0:
                workshop.removeMaterial(material, 1)

        # Checking the total of each material after removing.
        for material in workshop.materials:
            self.assertEqual(workshop.materials[material], 0)

    def testWorkshop(self):
        '''This function tests the display methods.'''
        with self.assertRaises(TypeError): 
            workshop.displayEnchantments()

        with self.assertRaises(TypeError):
            workshop.displayWeapons()

        with self.assertRaises(TypeError):
            workshop.displayMaterials()



unittest.main()

