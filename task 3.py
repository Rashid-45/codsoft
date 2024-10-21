import random
import string

def generate_password(length):
    # Define the character pool: letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by randomly selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired password length: "))
        
        if length < 4:
            print("Password length should be at least 4 characters.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Please enter a valid number for the password length.")

# Run the password generator
main()
