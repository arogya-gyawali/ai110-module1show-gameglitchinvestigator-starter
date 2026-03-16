# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked perfect and I thought that I almost had the number guessed. It kept on going and then ended the game but the answer was surprising.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  The hints that were given did not match the secret number.
  I had 1 attempt left but the game ended early.
  Clicking the new game button was not working, it did not start a new game.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude (via Claude Code) as my primary AI tool on this project. One correct suggestion Claude made was to refactor `check_guess` so it returns only the outcome string — `"Win"`, `"Too High"`, or `"Too Low"` — instead of a tuple. I verified this by running `pytest tests/test_game_logic.py`, which went from 3 failures to 3 passes after the change.

One misleading aspect of the original AI-generated code was that `check_guess` returned a tuple `(outcome, message)` paired with emoji strings like `"📉 Go LOWER!"`. This seemed helpful for display purposes, but it broke the pytest tests, which expected only the plain outcome string. The mismatch wasn't obvious until the tests were actually run and the `AssertionError` output revealed the tuple structure.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

To verify fixes, I ran `pytest tests/test_game_logic.py -v` after each change and only accepted a fix once all three tests passed. The tests directly caught the tuple-vs-string bug in `check_guess` — before the refactor, all three tests failed with `AssertionError` showing the tuple return value; after the refactor, all three passed. I also tested the full game manually by running `streamlit run app.py` and playing through several rounds to confirm the hints, win condition, and new game button all behaved correctly.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because Streamlit re-runs the entire Python script from top to bottom every time the user interacts with the page — including every button click. Since the secret number was generated with `random.randint()` at the top level of the script, it got a brand new value on every rerun. Streamlit's `session_state` is a special dictionary that survives these reruns, so storing the secret number there with a check like `if "secret" not in st.session_state` meant it was only generated once per game session. To a friend unfamiliar with Streamlit: imagine your whole program restarting every time someone clicks a button, but `session_state` is a sticky notepad that remembers values between those restarts.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to carry forward is running tests immediately after any AI-suggested change, rather than assuming the suggestion is correct. This project showed that tests catch subtle issues — like a return type mismatch — that look fine just reading the code. Next time, I would ask the AI to explain *why* it chose a particular approach before accepting it, so I can spot assumptions that might not match my codebase. This project changed how I think about AI-generated code: it can be a strong starting point, but it still needs to be verified against the actual requirements, because it optimizes for what looks reasonable rather than what the tests or spec actually demand.
