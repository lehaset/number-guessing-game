"""Unit tests for cli.py."""

import argparse

import pytest

from guessing_game.cli import build_parser, positive_int


@pytest.mark.parametrize("raw, expected", [("1", 1), ("7", 7)])
def test_positive_int_accepts_whole_numbers(raw, expected):
    assert positive_int(raw) == expected


@pytest.mark.parametrize("bad", ["0", "-3", "abc", "2.5"])
def test_positive_int_rejects_bad_values(bad):
    with pytest.raises(argparse.ArgumentTypeError):
        positive_int(bad)


def test_parser_defaults_to_none():
    args = build_parser().parse_args([])
    assert args.difficulty is None
    assert args.max_attempts is None


def test_parser_reads_options():
    args = build_parser().parse_args(["--difficulty", "hard", "--max", "5"])
    assert args.difficulty == "hard"
    assert args.max_attempts == 5


def test_parser_rejects_unknown_difficulty():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["--difficulty", "impossible"])