# Author: Haitian Jiang
# Date: 12/3/2023
# Description: This is the Creature class inherited from FieldInhabitant class.

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        """
               Constructor for the Creature class.

               Parameters:
               - x (int): Initial x-coordinate of the creature.
               - y (int): Initial y-coordinate of the creature.
               - symbol (str): The symbol representing the creature.
               """
        # Calling the constructor of the parent class (FieldInhabitant) using super()
        super().__init__(symbol)
        self._x = x
        self._y = y

    def get_x(self):
        """
        Get the x-coordinate of the creature.

        Returns:
        - int: The x-coordinate of the creature.
        """
        return self._x

    def set_x(self, x):
        """
        Set the x-coordinate of the creature.

        Parameters:
        - x (int): The new x-coordinate to set.
        """
        self._x = x

    def get_y(self):
        """
        Get the y-coordinate of the creature.

        Returns:
        - int: The y-coordinate of the creature.
        """
        return self._y

    def set_y(self, y):
        """
        Set the y-coordinate of the creature.

        Parameters:
        - y (int): The new y-coordinate to set.
        """
        self._y = y
