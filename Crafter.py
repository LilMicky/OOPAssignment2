from abc import ABC, abstractmethod


class Crafter(ABC):
    """
    An abstract class for classes to inherit from.

    Methods
    --------
    craft():
        Does not return anything.
    
    disassemble():
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
