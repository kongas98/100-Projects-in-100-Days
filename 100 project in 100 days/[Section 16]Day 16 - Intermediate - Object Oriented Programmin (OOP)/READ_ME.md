# Coffee Machine

This project simulates a coffee machine. The user can choose from different coffee options, pay for the coffee, and receive it if there are enough resources and the payment is sufficient. The coffee machine keeps track of resources and allows the user to see a report of the remaining resources and money earned.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Menu](#menu)
- [Resources](#resources)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [License](#license)

## Features
- Select from three types of coffee: espresso, latte, and cappuccino.
- Insert coins and receive change if necessary.
- Resource management: tracks water, coffee, and milk.
- Display a report of remaining resources and profit.
- Simple text-based user interface.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kongas98/coffeemachine.git
```
2. Navigate to the project directory:
```bash
cd coffeemachine
```
##Usage
Run the main.py script to start the coffee machine simulation:
```bash
python main.py
```
Follow the on-screen prompts to order coffee, insert coins, and view reports.

##Menu

The available coffee options and their ingredients are defined in the Menu class in menu.py:
1. Espresso
   * Water: 50ml
   * Milk: 0ml
   * Coffee: 18gr
   * Cost: $1.50
2. Latte
   * Water: 200ml
   * Milk: 150ml
   * Coffee: 24r
   * Cost: $2.50
3. Cappuccino
   * Water: 250ml
   * Milk: 50ml
   * Coffee: 24gr
   * Cost: $3.00

##Resources

The coffee machine tracks the following resources:
* Water: 300ml
* Milk: 200ml
* Coffee: 100gr

The resources are managed in the `coffeeMaker` class in `coffee_maker.py`

##Code Overview

###`main.py`

This is the main script that runs the coffee machine. It initializes the menu, coffee maker, and money machine. It also contains the main loop that prompts the user for input and processes coffee orders.

###`menu.py`

Contains the `MenuItem` and `Menu` classes:

* **`MenuItem`** models each coffee item with its ingredients and cost.
* **`Menu`** models the menu with a list of available coffee items and methods to get the items and find a specific drink by name.

###coffee_maker.py

Contains the CoffeeMaker class, which models the machine that makes the coffee. It includes methods to:
* Print a report of the current resources.
* Check if there are enough resources to make a particular drink.
* Deduct the required ingredients from the resources to make a coffee.

###`money_machine.py`

Contains the **MoneyMachine** class, which handles money transactions. It includes methods to:
* Print the current profit.
* Process inserted coins.
* Check if the payment is sufficient and handle change.

##Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

##License

This project is licensed under the MIT License.