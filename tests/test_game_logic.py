from logic_utils import check_guess, update_score

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


# FIX: Added score tests — none existed before. Covers win scoring formula,
# minimum floor, wrong-guess deductions, and accumulation.
def test_score_win_first_attempt():
    # win on attempt 1: 100 - 10*(1+1) = 80
    assert update_score(0, "Win", 1) == 80

def test_score_win_late_attempt():
    # win on attempt 9: 100 - 10*(9+1) = 0, hits minimum floor of 10
    assert update_score(0, "Win", 9) == 10

def test_score_too_high():
    assert update_score(0, "Too High", 1) == -5

def test_score_too_low():
    assert update_score(0, "Too Low", 1) == -5

def test_score_accumulates():
    score = update_score(0, "Too High", 1)    # -5
    score = update_score(score, "Too Low", 2) # -10
    score = update_score(score, "Win", 3)     # -10 + (100 - 40) = 50
    assert score == 50
