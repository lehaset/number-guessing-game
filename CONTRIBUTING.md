# Contributing

Thanks for your interest in improving the Number Guessing Game!

## Getting set up

```bash
git clone https://github.com/lehaset/number-guessing-game.git
cd number-guessing-game
python -m venv .venv
```

Activate the virtual environment, then install the project with its
development dependencies:

```bash
pip install -e .
pip install -r requirements-dev.txt
```

## Running the tests

```bash
pytest
```

All tests must pass before you open a pull request.

## Making changes

1. Create a branch: `git checkout -b feat/short-description`
2. Make your change and add tests for new behavior.
3. Run `pytest` and make sure everything is green.
4. Commit using [Conventional Commits](https://www.conventionalcommits.org/):
   `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, or `chore:`.
5. Push your branch and open a pull request describing what and why.

## Code style

- Follow PEP 8.
- Add type hints and docstrings to new functions.
- Keep functions small, with one job each.
- Keep game logic separate from input/output so it stays testable.

## Reporting bugs

Open an issue with the steps to reproduce, what you expected, and what
actually happened.