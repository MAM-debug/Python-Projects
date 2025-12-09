# Number Guessing Game 🎲

An interactive command-line game where you try to guess a random number chosen by the computer!

## How to Run
```bash
python numberguess.py
```

## Features
- Computer picks a random number
- Get hints (too high/too low)
- Track your attempts
- Input validation for numbers
- Error handling for invalid inputs

## How to Play

1. **Start the game:**
```
   WELCOME TO THE NUMBER GUESSING GAME BRO!
   Type a number: 100
```

2. **Set the range:**
   - Type the upper limit (number must be > 0)
   - Computer picks random number between 0 and your number

3. **Start guessing:**
```
   make a guess bro: 50
```

4. **Get feedback:**
   - "your guess is too high bro" - guess is higher than number
   - "your guess is too low bro" - guess is lower than number
   - "you got it right bro" - correct guess!

5. **See your score:**
```
   The number was: 42
   you made 7 attempts to guess the number
   THANKS FOR PLAYING!
```

## Example Gameplay
```
WELCOME TO THE NUMBER GUESSING GAME BRO!
Type a number: 100
make a guess bro: 50
your guess is too high bro
make a guess bro: 25
your guess is too low bro
make a guess bro: 37
your guess is too low bro
make a guess bro: 42
you got it right bro
The number was: 42
you made 4 attempts to guess the number
THANKS FOR PLAYING!
```

## Code Concepts Used

- **Input Validation:** `isdigit()` to check if input is a number
- **Random Number Generation:** `random.randrange()` for picking numbers
- **Loop Control:** `while True` for continuous guessing
- **Conditional Logic:** `if/elif/else` for comparing guesses
- **Error Handling:** `ValueError` for invalid inputs
- **String Conversion:** `str()` for displaying numbers

## Rules

- Enter a number greater than 0 as the range
- Your guesses must be between 0 and the range you set
- Invalid inputs will be rejected with error messages
- The game tracks how many attempts it takes to guess correctly

## Future Improvements

- Add difficulty levels (easy, medium, hard)
- Implement a scoring system based on attempts
- Add replay without restarting
- Save high scores to a file
- Add a time limit for each guess
