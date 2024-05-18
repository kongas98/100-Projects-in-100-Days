import os

# Define a list containing the alphabet letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to perform Caesar cipher encryption/decryption
def caesar(txt, shft, dir):
    cipher_txt = ""  # Initialize an empty string for the result
    for letter in txt:
        if letter.isalpha():  # Ignore spaces
            position = alphabet.index(letter)  # Find the position of the letter in the alphabet
            if dir == "encode":  # Check if the direction is 'encode'
                if (position + shft < 26):
                    new_letter = alphabet[position + shft]  # Find the new letter by shifting forwards
                    cipher_txt += new_letter  # Append the new letter to the result
                else:
                    # If the new position exceeds the length of the alphabet, wrap around
                    new_letter = alphabet[(position + shft) - 26]
                    cipher_txt += new_letter
            else:  # If the direction is 'decode'
                new_letter = alphabet[position - shft]  # Find the original letter by shifting backwards
                cipher_txt += new_letter  # Append the original letter to the result
        else:
            cipher_txt += letter  # Append spaces as they are
    return cipher_txt  # Return the final encrypted/decrypted text

# Main loop to repeatedly ask the user for input and process the encryption/decryption
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()  # Get the text and convert it to lowercase
    shift = int(input("Type the shift number:\n"))  # Get the shift number and convert it to an integer
    
    # Call the caesar function with the appropriate parameters and display the result
    if direction == "encode":
        print(f"The encoded text is {caesar(text, shift, direction)}")
    else:
        print(f"The decoded text is {caesar(text, shift, direction)}")
    
    # Ask the user if they want to run the program again
    reset = input("Would you like to encode/decode again? Type yes or no: ").lower()
    os.system("cls")  # Clear the screen (Windows only)
    if reset == "no":
        break  # Exit the loop if the user does not want to continue
