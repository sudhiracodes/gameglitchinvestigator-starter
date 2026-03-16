# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Game's purpose:

A number-guessing game where players try to find a randomly generated secret number within a limited amount of attempts and range based on difficulty level to maximize their score.

- Bugs we found: 

   - The "New Game" button failed to clean the board and restart the game.

   - The "Show hint" toggle did nothing.

   - Out-of-range guesses were accepted without any warning or restriction.

   - Easy mode was mapped incorrectly, giving fewer attempts than Normal mode.

   - The Easy mode UI prompt incorrectly told users to guess between 1 and 100 instead of 1 and 20.

   - Normal and Hard mode ranges were flipped (Normal was 1-100; Hard was 1-50).

   - The winning score update was delayed and didn't display immediately upon guessing correctly.

- Fixes applied:

   - Fixed `get_range_for_difficulty` and `attempt_limit_map` so difficulty scaling makes sense.

   - Programmed the "New Game" button to clear `st.session_state` and trigger `st.rerun()`.

   - Added input validation to block out-of-bounds guesses and trigger a warning.

   - Wired the hint toggle to properly display the "Too High/Too Low" messages.

   - Adjusted the logic flow so the score calculates and updates immediately on a win.

   - Stored the secret number in `st.session_state` so it doesn't regenerate on every button click.

## 📸 Demo
![alt text](<Screenshot 2026-03-15 at 11.06.00 PM.png>)
![alt text](<Screenshot 2026-03-15 at 11.06.45 PM.png>)
![alt text](<Screenshot 2026-03-15 at 11.04.30 PM.png>)


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
