import random 
import os

# Generate a random number between 1 and 100 for the game
PC_NUMBER = random.randint(1,100)

# Function to handle the guessing logic
def lower_higher(att, dif):
    while True:
        # Prompt user to make a guess
        str_guess = input("Make a guess: ")
        guess = int(str_guess)
        if att != 0 and guess > PC_NUMBER:
            # If guess is too high, decrease attempts and notify user
            print("Too high!")
            att -= 1
            if att == 0:
                # If no attempts left, return False
                return False, att
            print(f"You have {att} attempts to guess the number.")
        elif att != 0 and guess < PC_NUMBER:
            # If guess is too low, decrease attempts and notify user
            print("Too low!")
            att -= 1
            if att == 0:
                # If no attempts left, return False
                return False, att
            print(f"You have {att} attempts to guess the number.")
        else:
            # If guess is correct, return True
            return True, att

# Function to handle replay logic
def Replay():
    while True:
        # Ask user if they want to play again
        Play_Again = input("Would you like to play again? Type 'yes' or 'no': ").lower()
        if Play_Again == "yes" or Play_Again == "no":
            break
        print("Not an acceptable answer!")
    if Play_Again == "yes":
        # Restart the game if user wants to play again
        dif_level()
    exit()

# Function to start the game with selected difficulty
def Play_The_Game(dif):
    if dif == "easy":
        # Set attempts for easy difficulty
        attempts = 10
        print(f"You have {attempts} attempts to guess the number.")
    else:
        # Set attempts for hard difficulty
        attempts = 5
        print(f"You have {attempts} attempts to guess the number.")
    
    # Call the guessing logic function
    found, attempts = lower_higher(attempts, dif)
    if found:
        # If the number is found, congratulate the player
        print(f"Congrats! You found the number! It was {PC_NUMBER}!!")
    else:
        # If attempts run out, reveal the number
        print(f"Too bad! You lost! The number was {PC_NUMBER}...")
    
    # Prompt for replay
    Replay()

# Function to set the difficulty level and start the game
def dif_level():
    os.system("cls")  # Clear the screen (Windows only)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    while True:
        # Ask user to choose difficulty
        difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy" or difficulty == "hard":
            break
        print("Not an acceptable difficulty!")
    
    # Start the game with the selected difficulty
    Play_The_Game(difficulty)

# Start the game by prompting for difficulty level
dif_level()
