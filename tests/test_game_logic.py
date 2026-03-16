from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_negative_guess():
    # A negative guess below the secret should return "Too Low"
    result = check_guess(-10, 50)
    assert result == "Too Low"

def test_very_large_guess():
    # A very large guess above the secret should return "Too High"
    result = check_guess(1000000, 50)
    assert result == "Too High"

def test_decimal_guess():
    # A decimal guess above the secret should return "Too High"
    result = check_guess(50.5, 50)
    assert result == "Too High"
