correct_answers = 0
from logo import logo
from logo import vs
from game_data import data
import random
import os


correct_answers = 0
def candidates(x,candidate):
    print(f"Compare {x}: {candidate["name"]}, a {candidate["description"]}, from {candidate["country"]}.")

def generator():
    compare = random.choice(data)
    return compare

def Game(first,second):
    global correct_answers
    guess = input("Who has more followers?Type 'A' or 'B': ").lower()
    if guess == "a" and first['follower_count'] > second['follower_count']:
        correct_answers += 1
        print(f"Nice one! Your high score is {correct_answers}")
        return True
    elif guess == "a" and first['follower_count'] < second['follower_count']:
        print(f"You lost! Your high score is {correct_answers}")
        return False
    elif guess == "b" and second['follower_count'] > first['follower_count']:
        correct_answers += 1
        print(f"Nice one! Your high score is {correct_answers}")
        return True
    else:
        print(f"You lost! Your high score is {correct_answers}")
        return False

def Start():
    os.system("cls")
    print(logo)
    first_compare = generator()
    candidates("A",first_compare)
    print(vs)
    second_compare =  generator()
    candidates("B",second_compare)
    return Game(first_compare,second_compare)

def Replay():
    while True:
        Play_Again = input("Would you like to play again? Type 'y' or 'n': ")
        if Play_Again == "y" or Play_Again == "n":
            break
        print("Not an acceptable letter!")
    if Play_Again == "y":
        global correct_answers
        Start()
    exit()

correct_answers = 0
while True:
    if not Start():
        Replay()
    else:
        Start()





