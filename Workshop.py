class Workshop():
    """
    The main class where the enchanter, and forge class objects will be stored. As well as the weapons, enchantments, and materials.

    Attributes
    ----------
    forgeClass : Class
        The class used to forge weapons.

    enchanterClass: Class
        The class used to enchant weapons.

    Methods
    -------
    displayWeapons() :
        Returns a list of weapons stored in the workshop.

    displayEnchantments() :
        Returns a list of enchantments stored in the workshop.

    displayMaterials() :
        Returns a list of materials stored in the workshop.
    """
    def __init__(self, forgeClass, enchanterClass):
        self.forgeClass = forgeClass
        self.enchanterClass = enchanterClass
        self.weaponsList = []
        self.enchantmentsList = []

    def addWeapon(self, weapon):
        """
        Adds a new weapon to the workshop.

        Parameters:
            weapon (object) : The weapon object being added.
        """
        self.weaponsList.append(weapon)

    def addEnchantment(self, enchantment):
        """
        Adds a new enchantment to the workshop.

        Parameters:
            enchantment (object) : The enchantment object being added.
        """
        self.enchantmentsList.append(enchantment)

    def addMaterial(self, material, total):
        """
        Adds new materials to the workshop.

        Parameters:
            materials (object) : The materials object being added.
            total (int) : The amount of materials being added.
        """
        pass

    def removeWeapon(self, weapon):
        """
        Removes a weapon from the workshop.

        Parameters:
            weapon (object) : The weapon object being removed.
        """
        self.weaponsList.remove(weapon)

    def removeEnchantment(self, enchantment):
        """
        Removes an enchantment from the workshop.

        Parameters:
            enchantment (object) : The enchantment object being removed.
        """
        self.enchantmentsList.remove(enchantment)

    def removeMaterial(self, material, total):
        """
        Removes materials from the workshop.

        Parameters:
            materials (object) : The materials object being removed.
            total (int) : The amount of materials being removed.
        """
        pass
    
    def displayWeapons(self):
        """
        Returns a list of weapons stored in the workshop.

        Returns:
        Weapons (list): The list of weapons.
        """
        for weapon in self.weaponsList:
            if weapon.enchanted == False:
                print(f"The {weapon.name} is not enchanted. {weapon.attack()}")
            else:
                print(f"The {weapon.name} is imbued with a {weapon.enchantment.useEffect()}. {weapon.attack()}")

    def displayEnchantments(self):
        """
        Returns a list of enchantments stored in the workshop.

        Returns:
        Enchantments (list): The list of enchantments.
        """
        for enchant in self.enchantmentsList:
            print(f"A {enchant.name} enchantment is stored in the workshop.")

    def displayMaterials(self):
        """
        Returns a list of materials stored in the workshop.

        Materials (list): The list of materials.
        """
        for material in self.materialsDict:
            print(f"{material.name}: {material.total} remaining.")