import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock(r), paper(p), or scissors(s): ").lower()
        if user_choice in ["r", "p", "s"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock(r), paper(p), or scissors(s).")

def get_computer_choice():
    choices = ["r", "p", "s"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    play_game()
