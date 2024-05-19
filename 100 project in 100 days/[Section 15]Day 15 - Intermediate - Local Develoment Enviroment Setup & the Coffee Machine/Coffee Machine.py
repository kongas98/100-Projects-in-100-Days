"""MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}"""
from menu import *
import os

def return_to_the_menu():
    while True:
        return_to_menu = input("Return to main menu? Type 'y' or 'n': ").lower()
        if return_to_menu == "y" or return_to_menu == "n":
            break
    if return_to_menu == "y":
        Main_Menu()
def add_sugar():
    while True:
        sugar = input("Add Sugar? Type 'y' or 'n': ")
        if sugar == "y" or sugar == "n":
            break
    if sugar == "y":
        print("Sugar added!")

def not_enough_resources(order):
    if not(resources["water"] > MENU[order]["ingredients"]["water"]):
        print(f"There is not enough water.")
        return_to_the_menu()
    elif not(resources["coffee"] > MENU[order]["ingredients"]["coffee"]):
        print(f"There is not enough coffee")
        return_to_the_menu()
    else:
         print(f"There is not enough milk")
         return_to_the_menu()

def check_resources(order):
    if order == "espresso":
        if resources["water"] > MENU[order]["ingredients"]["water"] and resources["coffee"] > MENU[order]["ingredients"]["coffee"]:
                sum = coin_proccess()
                if sum == MENU[order]["cost"]:
                    print(f"Perfect! Your {order} is being made right now!")
                elif sum > MENU[order]["cost"]:
                    print(f"Great! Here are your change: {round(sum - MENU[order]["cost"],2)}")
                else:
                    print(f"Sorry... Not enough money! You need {MENU[order]["cost"]} and you inserted {sum} ")
                    return_to_the_menu()
                resources["water"] -= MENU[order]["ingredients"]["water"]
                resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
                return_to_the_menu()
        else:
            not_enough_resources(order)
    else:
        if resources["water"] > MENU[order]["ingredients"]["water"] and resources["coffee"] > MENU[order]["ingredients"]["coffee"] and resources["milk"] > MENU[order]["ingredients"]["milk"]:
                
                sum = coin_proccess()
                if sum == MENU[order]["cost"]:
                    print(f"Perfect! Your {order} is being made right now!")
                elif sum > MENU[order]["cost"]:
                    print(f"Great! Here are your change: {round(sum - MENU[order]["cost"],2)}")
                else:
                    print(f"Sorry... Not enough money! You need {MENU[order]["cost"]} and you inserted {sum} ")
                    return_to_the_menu()
                resources["water"] -= MENU[order]["ingredients"]["water"]
                resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
                resources["milk"] -= MENU[order]["ingredients"]["milk"]
                return_to_the_menu()
        else:
            not_enough_resources(order)

    if return_to_the_menu == "y":
        Main_Menu()
    else:
        exit()

def coin_proccess():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    sum_not_round = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    sum = round(sum_not_round,2)
    add_sugar()
    return sum

def Main_Menu():
    os.system("cls")
    print(logo)
    while True:
        order = input("What would you like? (espresso/latte/cappuccino):").lower()
        if order == "espresso" or order == "latte" or order == "cappuccino" or order == "report":
            break
        print("Not an acceptable order!")
    if order == "report":
        for key in resources:
            print(f"{key} : {resources[key]}")
        while True:
            back = input("Press 'y' to return to Menu: ").lower()
            if back == "y":
                break
        Main_Menu()

    else:
        print(f"{order} --> {MENU[order]["cost"]}")
        check_resources(order)

        



Main_Menu()