"""Core gameplay for the Number Guessing Game."""

import random

from guessing_game.scores import get_best_score, update_best_score
from guessing_game.ui import error, info, success, warning

DIFFICULTIES: dict[str, dict[str, int]] = {
    "easy": {"upper_bound": 50, "max_attempts": 10},
    "medium": {"upper_bound": 100, "max_attempts": 7},
    "hard": {"upper_bound": 500, "max_attempts": 9},
}


def choose_difficulty() -> str:
    """Prompt the player to pick a difficulty until the choice is valid.

    Returns:
        The difficulty name: "easy", "medium", or "hard".
    """
    print("Choose a difficulty:")
    print("  1. Easy   (1-50)")
    print("  2. Medium (1-100)")
    print("  3. Hard   (1-500)")

    choices = {"1": "easy", "2": "medium", "3": "hard"}
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice in choices:
            return choices[choice]
        error("Please enter 1, 2, or 3.")


def pick_number(upper_bound: int) -> int:
    """Pick a random secret number between 1 and upper_bound (inclusive)."""
    return random.randint(1, upper_bound)


def get_guess(upper_bound: int) -> int:
    """Prompt until the player enters a valid whole number in range.

    Args:
        upper_bound: The highest allowed guess. The lowest is always 1.

    Returns:
        A validated guess between 1 and upper_bound, inclusive.
    """
    while True:
        raw = input("Your guess: ").strip()

        if not raw:
            error("Please enter a number.")
            continue

        try:
            guess = int(raw)
        except ValueError:
            error("That's not a whole number. Try again.")
            continue

        if not 1 <= guess <= upper_bound:
            error(f"Please enter a number between 1 and {upper_bound}.")
            continue

        return guess


def check_guess(guess: int, secret_number: int) -> str:
    """Compare a guess with the secret number.

    Args:
        guess: The player's guess.
        secret_number: The number the computer picked.

    Returns:
        "low" if the guess is too small, "high" if too big,
        or "correct" if it matches.
    """
    if guess < secret_number:
        return "low"
    elif guess > secret_number:
        return "high"
    else:
        return "correct"


def play_round() -> None:
    """Play one full round: choose difficulty, then guess until win or loss."""
    difficulty = choose_difficulty()
    settings = DIFFICULTIES[difficulty]
    upper_bound = settings["upper_bound"]
    max_attempts = settings["max_attempts"]

    secret_number = pick_number(upper_bound)
    attempts = 0
    info(f"I'm thinking of a number between 1 and {upper_bound}.")
    info(f"You have {max_attempts} attempts.")
    best = get_best_score(difficulty)
    if best is not None:
        info(f"Best score on {difficulty}: {best}")

    while attempts < max_attempts:
        guess = get_guess(upper_bound)
        attempts += 1
        result = check_guess(guess, secret_number)

        if result == "low":
            warning("Too low!")
        elif result == "high":
            warning("Too high!")
        else:
            word = "attempt" if attempts == 1 else "attempts"
            success(f"You got it in {attempts} {word}!")
            if update_best_score(difficulty, attempts):
                success("New high score!")
            return

        remaining = max_attempts - attempts
        if remaining > 0:
            info(f"{remaining} left.")

    error(f"Out of attempts! The number was {secret_number}.")


def ask_play_again() -> bool:
    """Ask whether to play another round.

    Returns:
        True for yes, False for no. Re-prompts on anything else.
    """
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        error("Please enter y or n.")


def main() -> None:
    """Run the game: play rounds until the player chooses to stop."""
    info("Welcome to the Number Guessing Game!")
    while True:
        play_round()
        if not ask_play_again():
            info("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()