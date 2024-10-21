import random

def get_computer_choice():
    # Randomly choose between rock, paper, and scissors
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    # Determine the game outcome
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    while True:
        # Prompt the user to choose rock, paper, or scissors
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Generate a random choice for the computer
        computer_choice = get_computer_choice()
        print(f"The computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display the scores
        print(f"Score: You {user_score} - {computer_score} Computer")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final Score:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break

# Run the game
main()
