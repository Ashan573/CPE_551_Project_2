# Author: Haitian Jiang
# Date: 12/3/2023
# Description: This is the Rabbit class inherited from creature class.

from Creature import Creature

class Rabbit(Creature):
    """
    Constructor for the Rabbit class.

    Parameters:
    - x (int): Initial x-coordinate of the rabbit.
    - y (int): Initial y-coordinate of the rabbit.
    """
    # Calling the constructor of the parent class (Creature)
    def __init__(self, x, y):
        super().__init__(x, y, "R")
