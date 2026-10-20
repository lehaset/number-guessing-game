"""Unit tests for scores.py."""

import pytest

import scores


@pytest.fixture(autouse=True)
def temp_scores_file(tmp_path, monkeypatch):
    """Point SCORES_FILE at a temporary file so tests never touch real scores."""
    monkeypatch.setattr(scores, "SCORES_FILE", tmp_path / "highscores.json")


def test_load_scores_returns_empty_when_file_missing():
    assert scores.load_scores() == {}


def test_load_scores_returns_empty_when_file_corrupted():
    scores.SCORES_FILE.write_text("{{{", encoding="utf-8")
    assert scores.load_scores() == {}


def test_first_score_is_a_record():
    assert scores.update_best_score("easy", 6) is True
    assert scores.get_best_score("easy") == 6


def test_better_score_replaces_record():
    scores.update_best_score("easy", 6)
    assert scores.update_best_score("easy", 4) is True
    assert scores.get_best_score("easy") == 4


def test_worse_score_does_not_replace_record():
    scores.update_best_score("easy", 4)
    assert scores.update_best_score("easy", 8) is False
    assert scores.get_best_score("easy") == 4


def test_equal_score_is_not_a_new_record():
    scores.update_best_score("easy", 4)
    assert scores.update_best_score("easy", 4) is False


def test_get_best_score_returns_none_when_unset():
    assert scores.get_best_score("hard") is None


def test_difficulties_are_tracked_independently():
    scores.update_best_score("easy", 3)
    scores.update_best_score("hard", 9)
    assert scores.get_best_score("easy") == 3
    assert scores.get_best_score("hard") == 9