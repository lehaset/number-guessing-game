"""Unit tests for game.py."""

import pytest

from guessing_game.game import check_guess, get_guess, pick_number


@pytest.mark.parametrize(
    "guess, secret, expected",
    [
        (10, 50, "low"),
        (90, 50, "high"),
        (50, 50, "correct"),
        (1, 2, "low"),
        (500, 499, "high"),
    ],
)
def test_check_guess(guess, secret, expected):
    assert check_guess(guess, secret) == expected


def test_pick_number_stays_in_range():
    for _ in range(200):
        assert 1 <= pick_number(50) <= 50


def test_pick_number_with_upper_bound_one():
    assert pick_number(1) == 1


def feed_inputs(monkeypatch, answers):
    """Make input() return the given answers one at a time."""
    responses = iter(answers)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(responses))


@pytest.mark.parametrize("raw, expected", [("1", 1), ("25", 25), ("50", 50)])
def test_get_guess_accepts_valid_numbers(monkeypatch, raw, expected):
    feed_inputs(monkeypatch, [raw])
    assert get_guess(50) == expected


def test_get_guess_strips_whitespace(monkeypatch):
    feed_inputs(monkeypatch, ["  42  "])
    assert get_guess(50) == 42


@pytest.mark.parametrize("bad", ["", "abc", "3.5", "0", "51", "-4"])
def test_get_guess_reprompts_on_invalid_input(monkeypatch, bad):
    feed_inputs(monkeypatch, [bad, "25"])
    assert get_guess(50) == 25