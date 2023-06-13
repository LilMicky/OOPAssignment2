'''
File: Workshop.py
Description: This files contains the code for the workshop class.
Author: Harrison Jenkins
Student ID: 110348652
EmailID: jenhi001
This is my own work as defined by the University's Academic Misconduct Policy.
'''
from abc import ABC, abstractmethod
from Materials import *

class Crafter(ABC):
    """
    An abstract class for classes to inherit from.

    Methods
    --------
    craft() :
        Does not return anything.
    
    disassemble() :
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


class Enchanter(Crafter):
    """
    This class is a type of Crafter.

    Attributes
    ----------
    recipes : dictionary
        dictionary of enchantments alongside their effects.

    Methods
    --------
    craft(name, primaryMaterial, secondaryMaterial, materials):
        Returns an enchantment.

    disassemble(enchant, materials):
        Returns the materials from a disassembled enchantment.
    """
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

        # Removing used materials
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
    
    def enchant(self, weapon, newWeaponName, enchantment):
        """
        Enchants any given weapons.

        Parameters:
            weapon (object) : The weapon to be enchanted.
            enchantmentName (string) : The new name of the enchanted weapon.
            enchantment (string) : The enchantment to be applied.
        """
        weapon.name = newWeaponName
        weapon.enchantment = enchantment
        weapon.damage *= enchantment.magicDamage


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

    def calculateMagicDamage(self, primaryMaterial, catalystMaterial):
        """
        Calculates the damage of an enchantment.

        Parameters:
            primaryMaterial (string) : The primary material of the enchantment.
            catalystMaterial (string) : The catalyst material of the enchantment.

        Returns:
            magicDamage (float) : The damage of the enchantment.
                
        """
        return (primaryMaterial.magicPower * primaryMaterial.strength) + (catalystMaterial.magicPower * catalystMaterial.strength)

    def useEffect(self):
        """
        Uses the enchantment effect and deals the damage associated with the enchantment.

        Returns:
            effectMessage (string) : An effect message stating what enchantment was used and the effect it has.

        """
        return f"{self.name} enchantment and {self.effect}"

    def getName(self):
        """
        Retreives the name of the enchantment.

        Returns:
            name (string) : The name of the enchantment.
        """
        return self.__name

    def getMagicDamage(self):
        """
        Retreives the magic damage associated with the enchantment.

        Returns:
            magicDamage (float) : The magic damage of the enchantment.
        """
        return self.__magicDamage

    def getEffect(self):
        """
        Retrieves the effect associated with the enchantment.

        Returns:
            effect (string) : The effect of the enchantment.
        """
        return self.__effect

    def getPrimaryMaterial(self):
        """
        Retrieves the primary material associated with the enchantment.

        Returns:
            primaryMaterial (string) : The primary material of the enchantment.
        """
        return self.__primaryMaterial

    def getSecondaryMaterial(self):
        """
        Retrieves the catalyst material associated with the enchantment.

        Returns:
            catalystMaterial (string) : The catalyst material of the enchantment.
        """
        return self.__catalystMaterial

    def setName(self, name):
        """
        Sets the name of the enchantment.

        Parameters:
            name (string) : The name of the enchantment.
        """
        self.__name = name

    def setEffect(self, effect):
        """
        Sets the effect of the enchantment.

        Parameters:
            effect (string) : The effect of the enchantment.
        """
        self.__effect = effect

    def setMagicDamage(self, magicDamage):
        """
        Sets the magic damage of the enchantment.

        Parameters:
            magicDamage (float) : the magic damage of the enchantment.
        """
        self.__magicDamage = magicDamage

    # Properties for variables with getters and setters
    name = property(getName, setName)
    magicDamage = property(getMagicDamage, setMagicDamage)
    effect = property(getEffect, setEffect)

    # Properties for variables with just getters
    primaryMaterial = property(getPrimaryMaterial)
    catalystMaterial = property(getSecondaryMaterial)


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

    enchantment : string
        the enchantment attached to the weapon.
    
    enchanted : boolean
        the status of whether the weapon is enchanted.

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
        """
        # Assigning values to private variables.
        self.__name = name
        self.__damage = damage
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial
        self.__enchantment = ""

    def calculateDamage(self, primaryMaterial, catalystMaterial):
        """
        Calculates the damage of the weapon.

        Returns:
            damage (float) : The damage output.
        """
        if isinstance(primaryMaterial, Wood) and isinstance(catalystMaterial, Wood):
            return primaryMaterial.strength * catalystMaterial.strength
        elif isinstance(primaryMaterial, Metal) and isinstance(catalystMaterial, Metal):
            return (primaryMaterial.strength * primaryMaterial.purity) + (catalystMaterial.strength * catalystMaterial.purity)
        elif isinstance(primaryMaterial, Wood) and isinstance(catalystMaterial, Metal):
            return primaryMaterial.strength * (catalystMaterial.strength * catalystMaterial.purity)
        
        # In case of the primary material being metal and catalyst being wood.
        else:
            return (primaryMaterial.strength * primaryMaterial.purity) * catalystMaterial.strength
            
    def attack(self):
        """
        Attacks and deals the damage associated with the weapon.

        Returns:
            attackMessage (string) : An attack message displaying the damage output.
        """
        return f"It deals {self.damage:.2f} damage."

    def getName(self):
        """
        Retreives the name of the weapon.

        Returns:
            name (string) : The name of the weapon.
        """
        return self.__name

    def getDamage(self):
        """
        Retreives the damage of the weapon.

        Returns:
            damage (float) : The damage of the weapon.
        """
        return self.__damage

    def getEnchanted(self):
        """
        Retreives the enchanted status of the weapon.

        Returns:
            enchanted (boolean) : The enchanted status of the weapon.
        """
        return self.__enchanted

    def getPrimaryMaterial(self):
        """
        Retreives the primary material of the weapon.

        Returns:
            primaryMaterial (string) : The primary material of the weapon.
        """
        return self.__primaryMaterial

    def getSecondaryMaterial(self):
        """
        Retreives the catalyst material of the weapon.

        Returns:
            catalystMaterial (string) : The catalyst material of the weapon.
        """
        return self.__catalystMaterial

    def getEnchantment(self):
        """
        Retreives the enchantment of the weapon.

        Returns:
            enchanment (string) : The enchantment of the weapon.
        """
        return self.__enchantment

    def setName(self, name):
        """
        Sets the name of the weapon.

        Parameters:
            name (string) : The name of the weapon.
        """
        self.__name = name

    def setDamage(self, damage):
        """
        Sets the damage of the weapon.

        Parameters:
            damage (float) : The damage of the weapon.
        """
        self.__damage = damage

    def setEnchanted(self, enchanted):
        """
        Sets the enchanted status of the weapon.

        Parameters:
            enchanted (boolean) : The enchanted status of the weapon.
        """
        self.__enchanted = enchanted

    def setEnchantment(self, enchantment):
        """
        Sets the enchantment of the weapon.

        Parameters:
            enchantment (string) : The enchantment of the weapon.
        """
        self.__enchantment = enchantment

    # Properties for variables with getters and setters
    name = property(getName, setName)
    damage = property(getDamage, setDamage)
    enchanted = property(getEnchanted, setEnchanted)
    enchantment = property(getEnchantment, setEnchantment)

    # Properties for variables with just getters
    primaryMaterial = property(getPrimaryMaterial)
    catalystMaterial = property(getSecondaryMaterial)


class AntiDuplication():
    
    def display(self, list):

        # String to add each msg to then return
        emptyString = ""

        # Only materials are in a dict so if this is true, it has to be materials.
        if list.__class__.__name__ == "dict":
            for material in list:
                emptyString += f"{material}: {list[material]} remaining.\n"

            return emptyString
        
        if list[0].__class__.__name__ == "Weapon":
            for weapon in list:
                if weapon.enchantment == "":
                    emptyString += f"The {weapon.name} is not enchanted. {weapon.attack()}\n"
                else:
                    emptyString += f"The {weapon.name} is imbued with a {weapon.enchantment.useEffect()}. {weapon.attack()}\n"

            return emptyString
        
        for enchant in list:
                emptyString += f"A {enchant.name} enchantment is stored in the workshop.\n"

        return emptyString
    

class Workshop(AntiDuplication):
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

# Create a workshop, forge, enchanter.
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
print("--------------------------------Material Store--------------------------------")
print(workshop.displayMaterials())

# Crafts the following: Sword, Shield, Axe, Scythe, Bow, Wand and Staff weapons.
for weapon, materials in weaponBlueprints.items():
    craftedWeapon = workshop.forge.craft(
        weapon, materials[0], materials[1], workshop.materials)
    workshop.addWeapon(craftedWeapon)

# Disassemble the extra weapon.
workshop.removeWeapon(workshop.forge.disassemble(
workshop.weapons[7], workshop.materials))
print("------------------------------------Armoury-----------------------------------")
print(workshop.displayWeapons())

# Crafts the following: Holy, Lava, Pyro, Darkness, Cursed, Hydro and Venomous enchantments.
for enchantment, materials in enchantmentBlueprints.items():
    craftedEnchantment = workshop.enchanter.craft(
        enchantment, materials[0], materials[1], workshop.materials)
    workshop.addEnchantment(craftedEnchantment)

# Disassemble the extra enchantment.
workshop.removeEnchantment(workshop.enchanter.disassemble(
workshop.enchantments[7], workshop.materials))
print("------------------------------------Enchantments------------------------------------")
print(workshop.displayEnchantments())
print("-----------------------------------Material Store-----------------------------------")
print(workshop.displayMaterials())

# Enchant the following weapons: Sword, Shield, Axe, Scythe, Bow, Wand and Staff.
for i in range(len(enchantedWeapons)):
    workshop.enchanter.enchant(
    workshop.weapons[i], enchantedWeapons[i], workshop.enchantments[i])
print("-----------------------------------Enchanted Armoury----------------------------------")
print(workshop.displayWeapons())