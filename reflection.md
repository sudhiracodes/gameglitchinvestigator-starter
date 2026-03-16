# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game was very buggy and and many features of it weren't working as expected to work.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
Bugs we found:
1.⁠ ⁠New Game button doesn't work, doesn't clean and start a new game.
2. The show hint option doesn't do anything( go higher or lower).
3.⁠ ⁠When a user inputs a number that is out of range, the game still allows the input without an alert. The USER should be required to choose a number within the range.
4. The number of attempts for easy mode was lesser than normal along with the range.( easy shouldve been less tougher than normal i.e more attempts and smaller range)
5.⁠ ⁠Update the user prompt for Easy Mode. The When the user chooses Easy Mode, the range to guess should be 1-20. Currently, the game is prompting the user to guess a number between 1 and 100, so that range should also be fixed.
6.⁠ ⁠When we set the difficulty to hard, it says the range is 1-50, and when we set the difficulty to normal, it says the range is 1-100. This should be flipped.
7. Score being updated after the correct answer moves to history. Not immediately after gussing it correct.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Used Claude Copilot and Gemini
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The new game bug has been fixed correctly and verified. the reset occurs as expected.
The show hint works as expected.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The game begins with only 9 attempts sometimes and history is updated after that. 
even when range is between 1-20, the secret is generated randomly(above 20 as wellsuch as 34) but doesnt let you guess outside of the range(which it fixed) !!!!! major 
Collaborated with AI to fix this suggested fixes again.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Played the game manually again focusing on trying to taget the bug and seeing its behaviour working correctly or not. I notice other bugs that need to be fixed too.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
I ran manual check by playing the game to test the range bug(trying a range outside the given to see if it raises warning, and also the history list being updated properly) and also pytest to test the scoring and fixed the check guess tests as well.

- Did AI help you design or understand any tests? How?
Yes AI helped me understand how the score was computed and also pointed it the deduction logic on wrong answrs was a bug in logic that needed to be fixed again. Helped identify a bug and gave a fix for it when asked.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
It kept changing because of how Streamlit reruns the whole script every time you interact with it. Every time I clicked a button, it triggered the random number generator again instead of remembering the old one.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit basically has the memory of a goldfish—every time you click something, it forgets everything and restarts from line 1. "Session state" is like giving Streamlit a notepad so it can write down important variables (like the score) and remember them the next time it restarts.

- What change did you make that finally gave the game a stable secret number?
Wrapped the secret number generation inside an if "secret" not in st.session_state check. This forces the game to store the number in long-term memory and only generate a new one when a completely new game starts within the low-high range.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Next time, I will test the AI's generated logic in smaller, isolated chunks rather than trying to integrate a large block of code all at once. I also plan to ask the AI to explain why it is modifying state variables before I accept the changes.
 also testing the extreme edge cases first, like numbersoutside the 1-20 range, to see how the code breaks.

- What is one thing you would do differently next time you work with AI on a coding task?
I wouldn't trust the AI to understand the flow of a game. I'd have it write small helper functions instead of asking it to fix the whole app at once.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
That though AI is good at generating code, we still have to be the architect of the logic guiding AI to write the correct code and not rely on it blindly.
