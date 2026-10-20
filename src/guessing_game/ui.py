"""Helpers for colored terminal output."""

from colorama import Fore, init

init(autoreset=True)


def success(message: str) -> None:
    """Print a message in green (wins, new records)."""
    print(f"{Fore.GREEN}{message}")


def error(message: str) -> None:
    """Print a message in red (invalid input, losses)."""
    print(f"{Fore.RED}{message}")


def warning(message: str) -> None:
    """Print a message in yellow (too high / too low hints)."""
    print(f"{Fore.YELLOW}{message}")


def info(message: str) -> None:
    """Print a message in cyan (rules, status, greetings)."""
    print(f"{Fore.CYAN}{message}")