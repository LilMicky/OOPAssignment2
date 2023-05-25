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

    def calculateMagicDamage(self):
        """
        Calculates the damage of an enchantment.

        Returns:
            magicDamage (float) : The damage of the enchantment.
                
        """
        pass

    def useEffect(self):
        """
        Uses the enchantment effect and deals the damage associated with the enchantment.

        Returns:
            effectMessage (string) : An effect message stating what enchantment was used and the effect it has.

        """

    def getName(self):
        """
        Retreives the name of the enchantment.

        Returns:
            name (string) : The name of the enchantment.
        """
        pass

    def getMagicDamage(self):
        """
        Retreives the magic damage associated with the enchantment.

        Returns:
            magicDamage (float) : The magic damage of the enchantment.
        """
        pass

    def getEffect(self):
        """
        Retrieves the effect associated with the enchantment.

        Returns:
            effect (string) : The effect of the enchantment.
        """
        pass

    def getPrimaryMaterial(self):
        """
        Retrieves the primary material associated with the enchantment.

        Returns:
            primaryMaterial (string) : The primary material of the enchantment.
        """
        pass

    def getSecondaryMaterial(self):
        """
        Retrieves the catalyst material associated with the enchantment.

        Returns:
            catalystMaterial (string) : The catalyst material of the enchantment.
        """
        pass

    def setName(self, name):
        """
        Sets the name of the enchantment.

        Parameters:
            name (string) : The name of the enchantment.
        """
        pass

    def setEffect(self, effect):
        """
        Sets the effect of the enchantment.

        Parameters:
            effect (string) : The effect of the enchantment.
        """
        pass

    def setMagicDamage(self, magicDamage):
        """
        Sets the magic damage of the enchantment.

        Parameters:
            magicDamage (float) : the magic damage of the enchantment.
        """
        pass

    # Properties for variables with getters and setters
    name = property(getName, setName)
    magicDamage = property(getMagicDamage, setMagicDamage)
    effect = property(getEffect, setEffect)

    # Properties for variables with just getters
    primaryMaterial = property(getPrimaryMaterial)
    catalystMaterial = property(getSecondaryMaterial)