import json
from pathlib import Path

SCORES_FILE = Path("highscores.json")


def load_scores():
    if not SCORES_FILE.exists():
        return {}
    try:
        with SCORES_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_scores(scores):
    with SCORES_FILE.open("w", encoding="utf-8") as file:
        json.dump(scores, file, indent=2)


def get_best_score(difficulty):
    return load_scores().get(difficulty)


def update_best_score(difficulty, attempts):
    """Save attempts if it beats the record. Return True if it's a new record."""
    scores = load_scores()
    best = scores.get(difficulty)

    if best is None or attempts < best:
        scores[difficulty] = attempts
        save_scores(scores)
        return True
    return False