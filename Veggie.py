# Author: Aicheng Shan
# Date: 12/3/2023
# Description: This is the Veggie class inherited from FieldInhabitant class.

from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points):
        """
        Constructor for the Veggie class.

        Parameters:
        - name (str): The name of the vegetable.
        - symbol (str): The symbol representing the vegetable.
        - points (int): The points that the vegetable worth.
        """
        # Calling the constructor of the parent class FieldInhabitant.
        super().__init__(symbol)
        # Initializing private attributes for the vegetable's name and points.
        self._name = name
        self._points = points

    def __str__(self):
        """
        An overridden __str__() function that outputs the symbol, name, and points for the
        vegetable in an easy-to-read format

        Returns:
        - str: A formatted string containing the symbol, name, and points of the vegetable.
        """
        return f"{self.get_symbol()}: {self._name} {self._points} Points"

    def get_name(self):
        """
        Get the name of the vegetable.

        Returns:
        - str: The name of the vegetable.
        """
        return self._name

    def set_name(self, name):
        """
        Set the name of the vegetable.

        Parameters:
        - name (str): The new name to set for the vegetable.
        """
        self._name = name

    def get_points(self):
        """
        Get the points associated with the vegetable.

        Returns:
        - int: The points of the vegetable.
        """
        return self._points

    def set_points(self, points):
        """
        Set the points associated with the vegetable.

        Parameters:
        - points (int): The new points to set for the vegetable.
        """
        self._points = points
