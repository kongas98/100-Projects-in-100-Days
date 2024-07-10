# Importing the necessary modules
from turtle import Turtle, Screen
import random

# Setting up the screen for the turtle race
screen = Screen()
screen.setup(width=500, height=400)

# Prompting the user to input the number of players (up to 6)
number_of_players = screen.textinput("TURTLE RACE", "Write the number of players(Up to 6)")
nop = int(number_of_players)

# Initializing a list to store the players' bets
bet_list = []
for i in range(nop):
    # Prompting each player to place a bet on which turtle will win
    bet = screen.textinput("TURTLE RACE", "Place your bet on a Turtle(RED/GREEN/BLUE/YELLOW/PURPLE/ORANGE). Which one will win?")
    bet_list.append(bet)

# Defining the colors of the turtles and their starting positions
colors = ["red", "orange", "blue", "yellow", "purple", "green"]
y_positions = [-150, -100, -50, 0, 50, 100]

# Creating a list to store all the turtle objects
all_turtles = []

# Creating 6 turtles, setting their colors and positions, and adding them to the list
for turtle_index in range(6):
    RaceTurtle = Turtle(shape="turtle")
    RaceTurtle.penup()
    RaceTurtle.color(colors[turtle_index])
    RaceTurtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(RaceTurtle)

# Running the race
while True:
    # Selecting a random turtle to move
    rand_turtle = random.choice(all_turtles)
    # Moving the selected turtle a random distance between 1 and 5 units
    rand_distance = random.randint(1, 5)
    rand_turtle.forward(rand_distance)
    # Checking if the selected turtle has crossed the finish line
    if rand_turtle.xcor() > 230:
        # Storing the color of the winning turtle
        winning_color = rand_turtle.pencolor()
        break

# Announcing the result of the race
for bet_index in range(len(bet_list)):
    # Checking if any player's bet matches the winning turtle's color
    if winning_color == bet_list[bet_index]:
        print(f"Player{bet_index + 1} won! The {winning_color} turtle is the winner!")
        break
else:
    # If no player's bet matches the winning turtle's color, everyone loses
    print(f"Everyone lost! The {winning_color} turtle is the winner!")

# Waiting for a click on the screen to exit
screen.exitonclick()
