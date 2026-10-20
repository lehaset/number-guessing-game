import random

DIFFICULTIES = {
    "easy": {"upper_bound": 50, "max_attempts": 10},
    "medium": {"upper_bound": 100, "max_attempts": 7},
    "hard": {"upper_bound": 500, "max_attempts": 9},
}


def choose_difficulty():
    print("Choose a difficulty:")
    print("  1. Easy   (1-50)")
    print("  2. Medium (1-100)")
    print("  3. Hard   (1-500)")

    choices = {"1": "easy", "2": "medium", "3": "hard"}
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice in choices:
            return choices[choice]
        print("Please enter 1, 2, or 3.")


def pick_number(upper_bound):
    return random.randint(1, upper_bound)


def get_guess(upper_bound):
    while True:
        raw = input("Your guess: ").strip()

        if not raw:
            print("Please enter a number.")
            continue

        try:
            guess = int(raw)
        except ValueError:
            print("That's not a whole number. Try again.")
            continue

        if not 1 <= guess <= upper_bound:
            print(f"Please enter a number between 1 and {upper_bound}.")
            continue

        return guess


def check_guess(guess, secret_number):
    if guess < secret_number:
        return "low"
    elif guess > secret_number:
        return "high"
    else:
        return "correct"


def play_round():
    difficulty = choose_difficulty()
    settings = DIFFICULTIES[difficulty]
    upper_bound = settings["upper_bound"]
    max_attempts = settings["max_attempts"]

    secret_number = pick_number(upper_bound)
    attempts = 0
    print(f"I'm thinking of a number between 1 and {upper_bound}.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = get_guess(upper_bound)
        attempts += 1
        result = check_guess(guess, secret_number)

        if result == "low":
            print("Too low!")
        elif result == "high":
            print("Too high!")
        else:
            word = "attempt" if attempts == 1 else "attempts"
            print(f"You got it in {attempts} {word}!")
            return

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"{remaining} left.")

    print(f"Out of attempts! The number was {secret_number}.")

def ask_play_again():
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def main():
    print("Welcome to the Number Guessing Game!")
    while True:
        play_round()
        if not ask_play_again():
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()