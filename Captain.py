# Author:Haitian Jiang
# Date: 12/3/2023
# Description: This is the Captain class which inherited from Creature class.

from Creature import Creature


class Captain(Creature):
    def __init__(self, x, y):
        """
        Constructor for the Captain class.
        Parameters:
        - x (int): Initial x-coordinate of the Captain.
        - y (int): Initial y-coordinate of the Captain.
        """
        # Calling the constructor of the parent class (Creature) using super()
        super().__init__(x, y, "V")

        # Declare a new member variable to store an empty List containing all of the Veggie
        # objects the captain has collected should be declared
        self._veggies_collected = []

    def add_veggie(self, veggie):
        """
        Method to add a vegetable to the list of veggies collected by the Captain.

        Parameters:
        - veggie (str): The vegetable to be added.
        """
        self._veggies_collected.append(veggie)

    def get_veggies_collected(self):
        """
        Method to retrieve the list of veggies collected by the Captain.

        Returns:
        - list: List of veggies collected.
        """
        return self._veggies_collected

    def set_veggies_collected(self, veggies_collected):
        """
        Method to set the list of veggies collected by the Captain.

        Parameters:
        - veggies_collected (list): List of veggies to set as collected.
        """
        self._veggies_collected = veggies_collected
