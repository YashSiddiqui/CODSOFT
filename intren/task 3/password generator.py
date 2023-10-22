import random
import string

def generate_password(length):
    # Define the character sets for each complexity level
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on user input
    complexity = ""
    while not complexity:
        print("Select password complexity:")
        print("1. Easy (only lowercase letters)")
        print("2. Medium (lowercase + uppercase)")
        print("3. Strong (lowercase + uppercase + digits)")
        print("4. Ultra Strong (lowercase + uppercase + digits + special characters)")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            complexity = lowercase_letters
        elif choice == '2':
            complexity = lowercase_letters + uppercase_letters
        elif choice == '3':
            complexity = lowercase_letters + uppercase_letters + digits
        elif choice == '4':
            complexity = lowercase_letters + uppercase_letters + digits + special_characters
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

    # Generate the password
    password = ''.join(random.choice(complexity) for _ in range(length))
    return password

# Prompt the user for the desired password length
try:
    password_length = int(input("Enter the desired password length: "))
    if password_length <= 0:
        raise ValueError("Password length should be greater than 0.")

    generated_password = generate_password(password_length)

    # Display the generated password
    print("Generated Password:", generated_password)

    # Wait for user input before exiting
    input("Press Enter to exit...")

except ValueError as e:
    print("Invalid input:", e)
