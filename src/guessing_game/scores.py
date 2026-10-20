"""Load and save per-difficulty high scores in a JSON file."""

import json
from pathlib import Path
from typing import Optional

SCORES_FILE = Path("highscores.json")


def load_scores() -> dict[str, int]:
    """Read all saved scores from disk.

    Returns:
        A mapping of difficulty name to best attempt count. Returns an
        empty dict if the file is missing or unreadable.
    """
    if not SCORES_FILE.exists():
        return {}
    try:
        with SCORES_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_scores(scores: dict[str, int]) -> None:
    """Write the scores mapping to disk as formatted JSON."""
    with SCORES_FILE.open("w", encoding="utf-8") as file:
        json.dump(scores, file, indent=2)


def get_best_score(difficulty: str) -> Optional[int]:
    """Return the best attempt count for a difficulty, or None if unset."""
    return load_scores().get(difficulty)


def update_best_score(difficulty: str, attempts: int) -> bool:
    """Save attempts if it beats the current record.

    Args:
        difficulty: The difficulty level that was played.
        attempts: How many attempts the player needed to win.

    Returns:
        True if a new record was set, otherwise False.
    """
    scores = load_scores()
    best = scores.get(difficulty)

    if best is None or attempts < best:
        scores[difficulty] = attempts
        save_scores(scores)
        return True
    return False