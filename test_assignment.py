import unittest

from Workshop import *
from Crafter import *
from Enchanter import *
from Forge import *
from Weapon import *
from Enchantment import *
from Materials import *

class TestAssignment(unittest.TestCase):
    def testWeapon(self):
        weapon = Weapon("Vu", 69, "Wood", "Wood")

        self.assertEqual(weapon.name, "Vu")
        self.assertEqual(weapon.damage, 69)
        self.assertEqual(weapon.primaryMaterial, "Wood")
        self.assertEqual(weapon.catalystMaterial, "Wood")

    def testEnchantment(self):
        enchantment = Enchantment("Freshness", 69, "Stay fresh bah.", "Diamond", "Diamond")

        self.assertEqual(enchantment.name, "Freshness")
        self.assertEqual(enchantment.magicDamage, 69)
        self.assertEqual(enchantment.effect, "Stay fresh bah.")
        self.assertEqual(enchantment.primaryMaterial, "Diamond")
        self.assertEqual(enchantment.catalystMaterial, "Diamond")

    def testAdd(self):
        pass

    def testRemove(self):
        pass

unittest.main()

