from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(19)



screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()

