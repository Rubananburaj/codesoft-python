import random

# Function to get user's choice
def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

# Function to get computer's random choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner based on choices
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "Win"
    else:
        return "Lose"

# Initialize scores
user_score = 0
computer_score = 0

# Game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    # Display choices
    print("User choice:", user_choice)
    print("Computer choice:", computer_choice)

    # Determine and display the result
    result = determine_winner(user_choice, computer_choice)
    print("Result:", result)

    # Update scores
    if result == "Win":
        user_score += 1
    elif result == "Lose":
        computer_score += 1

    # Display scores
    print("User Score:", user_score)
    print("Computer Score:", computer_score)

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
