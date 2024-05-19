from art import logo

# Print the logo for the calculator
print(logo)

# Function to perform basic arithmetic operations
def Calc_Operations(oper, n1, n2):
    if oper == "+":  # Addition
        result = n1 + n2
    elif oper == "-":  # Subtraction
        result = n1 - n2
    elif oper == "/":  # Division
        result = n1 / n2
    else:  # Multiplication (default case)
        result = n1 * n2
    return result

# Function to handle user input and operations
def check_True(check, result):
    if check:  # If starting a new calculation
        first_number = float(input("What's the first number?: "))
    else:  # Continue with the previous result
        first_number = result
    
    # Get the operation from the user
    operation = input("Pick an operation (+),(-),(/),(*): ")
    next_number = float(input("What's the next number?: "))  # Get the next number
    
    # Perform the calculation
    result = Calc_Operations(operation, first_number, next_number)
    
    # Store the result in a dictionary
    calculator_dictionary["result"] = result
    
    # Print the current state of the calculator dictionary
    print(calculator_dictionary)
    
    # Display the result of the operation
    print(f"{first_number} {operation} {next_number} = {result}")
    
    # Ask if the user wants to continue with the current result or start anew
    next_operation = input("Press 'y' if you want to continue the operations or 'n' if you want to start anew: ").lower()
    if next_operation == "y":
        check = False  # Continue with the current result
    else:
        check = True  # Start a new calculation
    return check, result

# Initialize check to True and result to 0 for starting conditions
check = True
result = 0

# Main loop to repeatedly perform calculations
while True:
    if check:
        calculator_dictionary = {}  # Initialize an empty dictionary for each new calculation
    check, result = check_True(check, result)  # Perform the calculation and update the check and result variables
