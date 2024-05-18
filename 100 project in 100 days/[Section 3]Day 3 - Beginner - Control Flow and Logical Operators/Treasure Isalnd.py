print('''  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                               
           88           88                                 88  
           ""           88                                 88  
                        88                                 88  
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8 ''')
print("Welcome to Treasure Isalnd. Your misson is to find the treasure")
question = input("You are at a crossroad. Do you want to go 'left' or 'right'? ")

if question == "left":
    print("A guard has found you. Game over")
    exit()
else:
    question = input("You are at a lake. Do you want to 'wait' for the boat or 'swim'? ")
    if question == "swim":
        print("An alligator ate you! Game Over!")
        exit()
    else:
        question = input("You are at three doors. BLUE/RED/YELLOW. Which on will you take? ")
        if question == "Blue":
            print("Game Over")
            exit()
        elif question == "Red":
            print("Game Over")
            exit()
        else:
            print("You found the treasure!Congrats")