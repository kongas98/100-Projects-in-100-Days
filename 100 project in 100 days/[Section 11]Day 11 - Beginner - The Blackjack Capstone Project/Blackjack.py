from art import logo
import random

# List of possible card values in Blackjack
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to deal initial cards and calculate sums for player and computer
def dealing_and_summing(pl_cards, pc_cards, pl_sum, comp_sum):
    for _ in range(2):  # Deal two cards to both player and computer
        pl_cards.append(random.choice(cards))
        pl_sum += pl_cards[-1]
        pc_cards.append(random.choice(cards))
        comp_sum += pc_cards[-1]
    
    # Adjust for Aces if player goes over 21
    for i in range(len(pl_cards)):
        if pl_sum > 21 and pl_cards[i] == 11:
            pl_cards[i] = 1
            pl_sum -= 10

    # Adjust for Aces if computer goes over 21
    for i in range(len(pc_cards)):
        if comp_sum > 21 and pc_cards[i] == 11:
            pc_cards[i] = 1
            comp_sum -= 10

    return pl_cards, pc_cards, pl_sum, comp_sum

# Function to start the game based on user's choice
def Play(play):
    if play == "y":  # If the user wants to play
        # Initialize sums and card lists for player and computer
        player_sum = 0
        pc_sum = 0
        player_cards = []
        computer_cards = []

        # Deal initial cards and update sums
        player_cards, computer_cards, player_sum, pc_sum = dealing_and_summing(player_cards, computer_cards, player_sum, pc_sum)

        # Show initial cards to the player
        print(f"Your cards: {player_cards} Total Score: {player_sum}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Proceed to player's turn
        Player_Turn(player_sum, pc_sum, player_cards, computer_cards)
    else:  # If the user doesn't want to play
        exit()

# Function to handle replay logic
def Replay():
    while True:
        # Ask the user if they want to play again
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play in ["y", "n"]:
            break  # Break if input is valid
        print("Not an acceptable letter!")  # Prompt again if input is invalid
    Play(play)  # Start the game based on user's choice

# Function for the computer's turn
def Pc_Turn(pc_sum, player_sum, computer_cards):
    while pc_sum < 17:  # Computer draws cards until it has 17 or more
        computer_cards.append(random.choice(cards))
        pc_sum += computer_cards[-1]
        if pc_sum > 21 and computer_cards[-1] == 11:  # Adjust Ace value if necessary
            computer_cards[-1] = 1
            pc_sum -= 10

    # Show final computer's cards and sum
    print(f"Computer's cards: {computer_cards} Computer's Total Score: {pc_sum}")

    # Determine the winner
    if pc_sum > 21:
        print("Computer went OVER! YOU WIN!")
    elif pc_sum > player_sum:
        print("Computer WON!")
    elif pc_sum < player_sum:
        print("You WIN!")
    else:
        print("It's a TIE!")

    Replay()  # Ask if the user wants to play again

# Function for the player's turn
def Player_Turn(player_sum, pc_sum, player_cards, computer_cards):
    while True:
        # Ask the player if they want another card
        deal = input("Type 'y' to deal another card or 'n' to pass: ").lower()
        if deal in ["y", "n"]:
            break  # Break if input is valid
        print("Not an acceptable letter!")  # Prompt again if input is invalid
    
    if deal == "y":  # If player wants another card
        player_cards.append(random.choice(cards))
        player_sum += player_cards[-1]
        if player_sum > 21 and player_cards[-1] == 11:  # Adjust Ace value if necessary
            player_cards[-1] = 1
            player_sum -= 10

        # Show updated player's cards and sum
        print(f"Your cards: {player_cards} Total Score: {player_sum}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_sum > 21:  # If player goes over 21, they lose
            print("You went over! You lose!")
            Replay()  # Ask if the user wants to play again
        else:
            Player_Turn(player_sum, pc_sum, player_cards, computer_cards)  # Continue player's turn
    else:
        Pc_Turn(pc_sum, player_sum, computer_cards)  # Proceed to computer's turn

# Print the logo and start the game
print(logo)
Replay()  # Start the initial replay prompt to begin the game
