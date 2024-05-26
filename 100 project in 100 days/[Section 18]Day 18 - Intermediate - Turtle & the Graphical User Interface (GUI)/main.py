import turtle as turtle_module  # Importing the turtle module for drawing
import random  # Importing the random module for generating random choices

turtle_module.colormode(255)  # Setting the color mode to 255 for RGB colors
tim = turtle_module.Turtle()  # Creating a turtle object named 'tim'
tim.speed("fastest")  # Setting the drawing speed of the turtle to the fastest
tim.penup()  # Lifting the pen up so that the turtle doesn't draw lines while moving
tim.hideturtle()  # Hiding the turtle icon for a cleaner output

# List of RGB color tuples
color_list = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), 
    (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), 
    (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), 
    (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), 
    (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), 
    (174, 94, 97), (176, 192, 209)
]

# Positioning the turtle to start drawing
tim.setheading(225)  # Setting the heading of the turtle to 225 degrees
tim.forward(300)  # Moving the turtle forward by 300 units
tim.setheading(0)  # Setting the heading of the turtle to 0 degrees (facing right)

number_of_dots = 100  # Total number of dots to be drawn

# Loop to draw 100 dots
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))  # Drawing a dot of size 20 with a random color from the color_list
    tim.forward(50)  # Moving the turtle forward by 50 units

    # After every 10 dots, move the turtle up and back to the start of the next row
    if dot_count % 10 == 0:
        tim.setheading(90)  # Setting the heading of the turtle to 90 degrees (facing up)
        tim.forward(50)  # Moving the turtle forward by 50 units (which is up)
        tim.setheading(180)  # Setting the heading of the turtle to 180 degrees (facing left)
        tim.forward(500)  # Moving the turtle forward by 500 units (which is back to the start of the row)
        tim.setheading(0)  # Setting the heading of the turtle to 0 degrees (facing right)

# Creating a screen object to keep the window open until clicked
screen = turtle_module.Screen()
screen.exitonclick()  # Waiting for a click to close the screen
