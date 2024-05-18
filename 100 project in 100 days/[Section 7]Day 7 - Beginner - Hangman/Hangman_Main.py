import random
from Hangman_Art import stages
from Hangman_Words import word_list
import os 
display = []
chosen_word = random.choice(word_list)
for i in range(len(chosen_word)):
    display.append("_")

stage = -1
print(stages[stage])

for i in range(len(display)):
    print(display[i]," ",end="")

while True:
    guess = input("\nWrite a letter: ").lower()
    os.system('cls')
    for char in chosen_word:
        if guess == char:
            found = True
            break
        else:
            found = False
    if found and guess not in display:
        print("YES!")
        print(stages[stage])
        for char in range(len(display)):
            if guess == chosen_word[char]:
                display[char] = guess
        for i in range(len(display)):
            print(display[i]," ",end="")
    elif found and guess in display:
        print("\nLetter Already Exists!")
        print(stages[stage])
        for i in range(len(display)):
            print(display[i]," ",end="")
    else:
        if stage > -7:
            print(stages[stage])
            stage -=  1
        else:
            game_won = False
            break

        print("NO")
        for i in range(len(display)):
            print(display[i]," ",end="")

    if "_" not in display:
        game_won = True
        break
if game_won:
    print(stages[stage])
    print("You win!!\n\nThe word was ",chosen_word)
else:
    print(stages[stage])
    print("You lose!!\n\nThe word was ",chosen_word)

