"""Command-line interface for the Number Guessing Game."""

import argparse
from typing import Optional, Sequence

from guessing_game.game import DIFFICULTIES
from guessing_game.game import main as run_game


def positive_int(value: str) -> int:
    """Parse a whole number of at least 1 (used as an argparse type)."""
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value!r} is not a whole number") from None
    if number < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return number


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="guessing-game",
        description="A number guessing game with difficulty levels and high scores.",
    )
    parser.add_argument(
        "-d",
        "--difficulty",
        choices=list(DIFFICULTIES),
        help="skip the menu and play at this difficulty",
    )
    parser.add_argument(
        "-m",
        "--max",
        dest="max_attempts",
        type=positive_int,
        help="override the maximum number of attempts",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Parse command-line arguments and start the game."""
    args = build_parser().parse_args(argv)
    run_game(difficulty=args.difficulty, max_attempts=args.max_attempts)


if __name__ == "__main__":
    main()