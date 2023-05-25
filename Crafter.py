'''
File: Crafter.py
Description: This files contains the code for the crafter class.
Author: Harrison Jenkins
Student ID: 110348652
EmailID: jenhi001
This is my own work as defined by the University's Academic Misconduct Policy.
'''


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
