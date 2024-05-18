import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

title = '''
Welcome to ROCK/PAPER/SCISSORS

To start type "0": '''
print(title,end="")
start = int(input())
if start == 0:
    Player_Selection = int(input("Rock/Paper/Scissors (0,1,2): "))
    PC_Selection = random.randint(0,2)
    if Player_Selection == 0:
        print("\nYou chose\n", rock)
    elif Player_Selection == 1:
        print("\nYou chose\n",paper)
    else:
        print("\nYou chose\n",scissors)
    if PC_Selection == 0:
        print("\nPC chose\n", rock)
    elif PC_Selection == 1:
        print("\nPC chose\n",paper)
    else:
        print("\nPC chose\n",scissors)
    if Player_Selection - PC_Selection > 0 or Player_Selection - PC_Selection == -2:
        print("You win!!!")
    elif Player_Selection - PC_Selection < 0 or Player_Selection - PC_Selection == 2:
        print("You lose!!!")
    else:
        print("It's a TIE!!!")



