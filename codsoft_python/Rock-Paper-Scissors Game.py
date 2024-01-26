import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "You lose!"

def print_score(user_score, computer_score):
    print(f"\nUser Score: {user_score} | Computer Score: {computer_score}\n")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = input("Enter your choice (1/2/3/4): ").lower()

        if user_choice == '4':
            break  

        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        if user_choice in ['1', '2', '3']:
            user_choice = choices[int(user_choice) - 1]
            result = determine_winner(user_choice, computer_choice)
            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")
            print(result)

            if result == "You win!":
                user_score += 1
            elif result == "You lose!":
                computer_score += 1

            print_score(user_score, computer_score)
        else:
            print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    play_game()
