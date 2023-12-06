# Author: Haitian Jiang
# Date: 12/4/2023
# Description: This program is the main function of the game.

# Importing the GameEngine class
from GameEngine import GameEngine

# Main function to execute the Captain Veggie game
def main():
    # Create an instance of the GameEngine class
    game_engine = GameEngine()

    # Display the game introduction
    game_engine.initializeGame()

    # Display the game introduction
    game_engine.intro()

    # Get the initial count of remaining veggies
    remaining_veggies = game_engine.remainingVeggies()

    while remaining_veggies > 0:
        # Continue the loop until no more veggies remaining in the Field list.
        print(f"\n{remaining_veggies} veggies remaining. Current score: {game_engine.getScore()}")
        game_engine.printField()

        # Move the Rabbits and the Captain objects based on user input
        game_engine.moveRabbits()
        game_engine.moveCaptain()

        # Update the number of remaining veggies
        remaining_veggies = game_engine.remainingVeggies()

    # Display the game over message and the player's score
    game_engine.gameOver()

    # Update the high score file
    game_engine.highScore()

if __name__ == "__main__":
    main()
