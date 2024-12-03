import random

def get_user_guess():
    """Prompt the user to enter a guess."""
    while True:
        try:
            return int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    """Main game logic."""
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

def main():
    """Start the program."""
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

