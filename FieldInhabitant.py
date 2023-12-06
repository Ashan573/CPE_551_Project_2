# Author: Aicheng Shan
# Date: 12/3/2023
# Description: This is the FieldInhabitant class.

class FieldInhabitant:
    def __init__(self, symbol):
        """
        Constructor for the FieldInhabitant class.

        Parameters:
        - symbol (str): The symbol representing the field inhabitant(captain, vegetable, rabbits, etc).
        """
        # Initialize the symbol attribute for the inhabitant
        self._symbol = symbol

    def get_symbol(self):
        """
        Getter function for the symbol parameter.

        Returns:
        - str: The symbol of the inhabitant.
        """
        return self._symbol

    def set_symbol(self, symbol):
        """
        Setter function for the symbol parameter.

        Parameters:
        - symbol (str): The new symbol to set.
        """
        self._symbol = symbol
