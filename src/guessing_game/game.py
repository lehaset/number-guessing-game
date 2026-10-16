import random


def pick_number():
    return random.randint(1, 100)


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
    secret_number = pick_number()
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "low":
            print("Too low!")
        elif result == "high":
            print("Too high!")
        else:
            print("You got it!")
            break


if __name__ == "__main__":
    main()