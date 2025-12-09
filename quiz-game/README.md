# Quiz Game - Logic Gates Edition 🎮

A fun and interactive command-line quiz game that tests your knowledge of digital logic gate IC numbers.

## 📋 Project Overview

This is a beginner-friendly Python project that demonstrates fundamental programming concepts like variables, conditionals, user input, and score tracking. Players answer 4 questions about integrated circuit (IC) logic gates and earn points for correct answers.

## ✨ Features

- **Interactive Gameplay** - Real-time user interaction through the command line
- **Score Tracking** - Keeps track of correct answers
- **Exit Option** - Players can quit before playing
- **Instant Feedback** - Immediate response for correct and wrong answers
- **Final Score Display** - Shows total correct answers at the end

## 🎯 Questions Included

The quiz contains 4 questions about IC logic gates:

1. **NAND Gate** - IC number: 7400
2. **AND Gate** - IC number: 7408
3. **XOR Gate** - IC number: 7486
4. **NOT Gate** - IC number: 7404

## 💻 Requirements

- Python 3.6 or higher
- No additional libraries needed (uses only built-in functions)

## 🚀 How to Run

### Option 1: Using Command Line
```bash
python project1.py
```

### Option 2: Using VS Code
1. Open the file in VS Code
2. Press `Ctrl + F5` to run
3. Or click the Run button (play icon) at the top right

## 📖 How to Play

1. **Start the game:**
   ```
   Welcome to my quiz
   hey bro wanna play game???
   ```

2. **Choose to play:**
   - Type `yes` to start playing
   - Type anything else to quit

3. **Answer questions:**
   ```
   what is the ic number of NAND?
   ```
   - Type the correct IC number
   - Get instant feedback

4. **See your score:**
   ```
   you got 4 questions correct
   THANKS FOR PLAYING!
   ```

## 📊 Example Gameplay

```
Welcome to my quiz
hey bro wanna play game???yes
okay ! come on lets play bro
what is the ic number of NAND?7400
cool correct answer
what is the ic number of AND?7408
cool correct answer
what is the ic number of XOR?7486
cool correct answer
what is the ic number of NOT?7404
cool correct answer
you got 4 questions correct
THANKS FOR PLAYING!
```

## 🔧 Code Breakdown

**Main Components:**

1. **Welcome Message** - Greets the player
2. **Play Decision** - Asks if user wants to play
3. **Score Variable** - Tracks correct answers
4. **Question Loop** - Repeats for each question
5. **Answer Validation** - Checks if answer is correct
6. **Final Score** - Displays total points

**Key Concepts Used:**
- Variables: `playing`, `score`, `answer`
- Conditionals: `if`, `else` statements
- User Input: `input()` function
- String Methods: `.lower()` for case-insensitive input
- Type Conversion: `str()` for score display
- Built-in Functions: `print()`, `quit()`

## 🎓 Learning Outcomes

By studying this project, you'll learn:
- How to get user input
- How to make decisions with if/else
- How to track data with variables
- How to give feedback to users
- Basic game loop structure

## 📈 Possible Improvements

- Add a time limit for each question
- Create a question bank and randomize questions
- Add difficulty levels (easy, medium, hard)
- Save high scores to a file
- Add more questions
- Create a graphical interface with Streamlit
- Add a multiplayer option
- Store player data in a database

## 🌐 Convert to Web App

This quiz can be easily converted to a web application using Streamlit:

```python
import streamlit as st

st.title("Logic Gates Quiz Game")
# Add Streamlit widgets here
```

## 📝 Code Comments

The code is simple and beginner-friendly. Future versions can include:
- Detailed comments explaining each section
- Function definitions for better organization
- Data structures like dictionaries for questions

## 🤝 Contributing

Feel free to fork this project and add improvements:
- More questions
- Better error handling
- User authentication
- Leaderboard system

## 📄 License

This project is free to use for educational purposes.

## 👨‍💻 Author

Created as a beginner Python learning project.

## 📞 Support

If you have questions about the code:
- Review the code comments
- Test with different inputs
- Break down each section to understand it better

---

**Happy Learning! 🚀**