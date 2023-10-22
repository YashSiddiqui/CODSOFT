# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    # Prompt the user for input
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter 'q' to end the program")

    user_input = input(": ")

    if user_input == "q":
        break
    elif user_input in ("+", "-", "*", "/"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "+":
            print("Result:", add(num1, num2))
        elif user_input == "-":
            print("Result:", subtract(num1, num2))
        elif user_input == "*":
            print("Result:", multiply(num1, num2))
        elif user_input == "/":
            print("Result:", divide(num1, num2))

        # Ask the user whether they want to continue
        while True:
            choice = input("Do you want to do more calculations? (y/n): ").lower()
            if choice in ("y", "n"):
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")

        if choice == "n":
            break
    else:
        print("Invalid input. Please enter a valid operation.")
