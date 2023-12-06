# Author: Haitian Jiang and Aicheng Shan
# Date: 12/4/2023
# Description: This program defines the movement of objects and the points collected.

import random
import pickle
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit


class GameEngine:
    __NUMBEROFVEGGIES = 30  # Define the number of veggies in the field.
    __NUMBEROFRABBITS = 5  # Define the number of rabbits in the field.
    __HIGHSCOREFILE = "highscore.data"  # Initialize the high score data.

    def __init__(self):
        # Constructor for the GameEngine class.
        self._field = []  # An empty list representing the game field
        self._rabbits = []  # List to store Rabbit objects
        self._captain = None  # Variable to store the Captain object, initialized to None.
        self._possible_veggies = []   # List to store Veggie objects
        self._score = 0     # Variable to store the score, initialized to 0

    def initVeggies(self):
        # Initialize the veggies
        while True:
            try:
                # Get the name of the veggie file from the user
                veggie_file_name = input("Enter the name of the veggie file: ")
                with open(veggie_file_name, 'r') as file:
                    # Read the dimensions of the game field from the first line of the file
                    first_line = file.readline().strip().split(',')
                    rows, cols = int(first_line[1]), int(first_line[2])
                    self._field = [[None] * cols for _ in range(rows)]

                    # Create Veggie objects from the file and add them to the list of possible veggies
                    for line in file:
                        veggie_info = line.strip().split(',')
                        veggie = Veggie(veggie_info[0], veggie_info[1], int(veggie_info[2]))
                        self._possible_veggies.append(veggie)

                    # Place random veggies on the field list.
                    for _ in range(self.__NUMBEROFVEGGIES):
                        while True:
                            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
                            if self._field[row][col] is None:
                                self._field[row][col] = random.choice(self._possible_veggies)
                                break
                    break
            except FileNotFoundError:
                print("VeggieFile.csv does not exist!")

    # Method to initialize the Captain object
    def initCaptain(self):
        rows, cols = len(self._field), len(self._field[0])
        while True:
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
            if self._field[row][col] is None:
                self._captain = Captain(row, col)
                self._field[row][col] = self._captain
                break

     # Method to initialize the Rabbit objects
    def initRabbits(self):
        rows, cols = len(self._field), len(self._field[0])
        for _ in range(self.__NUMBEROFRABBITS):
            while True:
                row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
                if self._field[row][col] is None:
                    rabbit = Rabbit(row, col)
                    self._rabbits.append(rabbit)
                    self._field[row][col] = rabbit
                    break

    # Method that calls other initialization methods
    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    # Method that examines the field 
    def remainingVeggies(self):
        return sum(len(row) - row.count(None) - sum(1 for item in row if isinstance(item, Rabbit)) -sum(1 for item in row if isinstance(item, Captain))for row in self._field)

    # Method to welcome the player and print introduction to the game
    def intro(self):
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest"
              "as many vegetables as possible before the rabbits eat them"
              "all! Each vegetable is worth a different number of points"
              "so go for the high score!")
        print("\nThe vegetables are:")
        for veggie in self._possible_veggies:
            print(veggie)
        print("Captain Veggie is V, and the rabbits are R's.")
        print("Good luck!")

    # Method to print the current state of the game field
    def printField(self):
        rows, cols = len(self._field), len(self._field[0])
        print("#" + "#" * (cols * 3) + "#")
        for row in self._field:
            print("#", end="")
            for item in row:
                if item is None:
                    print("   ", end="")
                else:
                    print(f" {item.get_symbol()} ", end="")
            print("#\n", end="")
        print("#" + "#" * (cols * 3) + "#")

    # Method to get the current score
    def getScore(self):
        return self._score

    # Method to move Rabbits objects on the field
    def moveRabbits(self):
        rows, cols = len(self._field), len(self._field[0])
        for rabbit in self._rabbits:
            while True:
                direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)])
                new_row, new_col = rabbit.get_x() + direction[0], rabbit.get_y() + direction[1]
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if isinstance(self._field[new_row][new_col], Veggie):
                        self._field[new_row][new_col] = None
                    elif self._field[new_row][new_col] is None:
                        self._field[rabbit.get_x()][rabbit.get_y()] = None
                        rabbit.set_x(new_row)
                        rabbit.set_y(new_col)
                        self._field[new_row][new_col] = rabbit
                        break
