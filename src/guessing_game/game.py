import random

DIFFICULTIES = {
    "easy": 50,
    "medium": 100,
    "hard": 500,
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


def get_guess():
    return int(input("Your guess: "))


def check_guess(guess, secret_number):
    if guess < secret_number:
        return "low"
    elif guess > secret_number:
        return "high"
    else:
        return "correct"


def main():
    difficulty = choose_difficulty()
    upper_bound = DIFFICULTIES[difficulty]
    secret_number = pick_number(upper_bound)
    attempts = 0
    print(f"I'm thinking of a number between 1 and {upper_bound}.")

    while True:
        guess = get_guess()
        attempts += 1
        result = check_guess(guess, secret_number)

        if result == "low":
            print("Too low!")
        elif result == "high":
            print("Too high!")
        else:
            word = "attempt" if attempts == 1 else "attempts"
            print(f"You got it in {attempts} {word}!")
            break


if __name__ == "__main__":
    main()