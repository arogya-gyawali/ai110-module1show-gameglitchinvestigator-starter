def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# AI Collaboration Note: The original check_guess function returned a tuple (outcome, message),
# e.g. ("Too High", "📉 Go LOWER!"). However, the pytest tests expected only the outcome string.
# Claude (AI) assisted in identifying this mismatch and refactored the function to return only
# "Win", "Too High", or "Too Low". The try/except block and emoji messages were also removed
# as they were unnecessary once the logic was simplified to work with integer comparisons.
def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome string.

    Returns: "Win", "Too High", or "Too Low"
    """
    if guess == secret:
        return "Win"
    elif guess > secret:
        return "Too High"
    else:
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
