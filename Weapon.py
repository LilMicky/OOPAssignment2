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

        Returns:
            weapon (object) : A weapon object.
        """
        # Assigning values to private variables.
        self.__name = name
        self.__damage = damage
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial
        self.__enchantment = ""
        self.__enchanted = False

    def calculateDamage(self):
        """
        Calculates the damage of the weapon.

        Returns:
            damage (float) : The damage output.
        """
        pass

    def attack(self):
        """
        Attacks and deals the damage associated with the weapon.

        Returns:
            attackMessage (string) : An attack message displaying the damage output.
        """
        pass

    def getName(self):
        """
        Retreives the name of the weapon.

        Returns:
            name (string) : The name of the weapon.
        """
        pass

    def getDamage(self):
        """
        Retreives the damage of the weapon.

        Returns:
            damage (float) : The damage of the weapon.
        """
        pass

    def getEnchanted(self):
        """
        Retreives the enchanted status of the weapon.

        Returns:
            enchanted (boolean) : The enchanted status of the weapon.
        """
        pass

    def getPrimaryMaterial(self):
        """
        Retreives the primary material of the weapon.

        Returns:
            primaryMaterial (string) : The primary material of the weapon.
        """
        pass

    def getSecondaryMaterial(self):
        """
        Retreives the catalyst material of the weapon.

        Returns:
            catalystMaterial (string) : The catalyst material of the weapon.
        """
        pass

    def getEnchantment(self):
        """
        Retreives the enchantment of the weapon.

        Returns:
            enchanment (string) : The enchantment of the weapon.
        """
        pass

    def setName(self, name):
        """
        Sets the name of the weapon.

        Parameters:
            name (string) : The name of the weapon.
        """
        pass

    def setDamage(self, damage):
        """
        Sets the damage of the weapon.

        Parameters:
            damage (float) : The damage of the weapon.
        """
        pass

    def setEnchanted(self, enchanted):
        """
        Sets the enchanted status of the weapon.

        Parameters:
            enchanted (boolean) : The enchanted status of the weapon.
        """
        pass

    def setEnchantment(self, enchantment):
        """
        Sets the enchantment of the weapon.

        Parameters:
            enchantment (string) : The enchantment of the weapon.
        """
        pass

    # Properties for variables with getters and setters
    name = property(getName, setName)
    damage = property(getDamage, setDamage)
    enchanted = property(getEnchanted, setEnchanted)
    enchantment = property(getEnchantment, setEnchantment)

    # Properties for variables with just getters
    primaryMaterial = property(getPrimaryMaterial)
    catalystMaterial = property(getSecondaryMaterial)