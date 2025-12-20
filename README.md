# Python Projects 🐍
A collection of Python learning projects from basic to advanced.

## Projects

### 1. Quiz Game 🎮
An interactive command-line quiz game about IC logic gates.
- **Location:** `quiz-game/`
- **File:** `project1.py`
- **Features:** Score tracking, instant feedback, 4 questions
- [Read more](https://github.com/MAM-debug/Python-Projects/commit/8dde53986bd360e0dc0f73847da42730d4750d29)

### 2. Number Guessing Game 🎲
Guess the random number game with hints and scoring system.
- **Location:** `numberguess/`
- **File:** `numberguess.py`
- **Features:** Input validation, attempt tracking, difficulty range
- [Read more](https://github.com/MAM-debug/Python-Projects/commit/de1bbe4fb66eb944c932460a771e76ddca196aea)

### 3. Weather App 🌤️
Real-time weather application built with Streamlit and OpenWeatherMap API.
- **Location:** `Streamlit/`
- **File:** `project3.py`
- **Features:**
  - Search weather by city name
  - Real-time temperature (Celsius)
  - Humidity and wind speed
  - Weather description
  - Error handling
- [Read more](https://github.com/MAM-debug/Python-Projects/commit/618b3fc3e1613d21e12cb6312013766383bd1587)

### 4. CSV Data Explorer 📊
Interactive data analysis web application for exploring CSV files.
- **Location:** `Csv Explorer/Streamlit/`
- **File:** `project4.py`
- **Features:**
  - File upload with drag-and-drop
  - Interactive data table display
  - Dataset dimensions (rows & columns)
  - Column information and data types
  - Statistical summary (mean, median, std, quartiles)
  - Missing values analysis with percentages
- - [Read more](Csv Explorer/README.md)

---

## Getting Started
Each project folder has its own README with detailed instructions.

To run any project:

### Command Line Projects
```bash
cd quiz-game
python project1.py

cd number guess
python project2.py
```

### Web Apps (Weather App & CSV Explorer)
```bash
# Weather App
cd Streamlit
pip install streamlit requests
streamlit run project3.py

# CSV Data Explorer
cd "Csv Explorer/Streamlit"
pip install streamlit pandas
streamlit run project3.py
```

---

## Technologies Used
- **Python 3** - Core language
- **Built-in libraries** - os, random, etc.
- **Streamlit** - Web framework (Weather App, CSV Explorer)
- **Requests** - HTTP library (Weather App)
- **Pandas** - Data manipulation (CSV Explorer)
- **OpenWeatherMap API** - Weather data (Weather App)

---

## Project Structure
```
python-projects/
├── README.md (this file)
├── quiz-game/
│   ├── project1.py
│   └── README.md
├── numberguess/
│   ├── numberguess.py
│   └── README.md
├── Streamlit/
│   ├── project3.py
│   ├── README.md
│   └── README_SHORT.md
└── Csv Explorer/
    └── Streamlit/
        ├── project4.py
        └── README.md
```

---

## How to Use This Repository

1. **Clone the repository**
   ```bash
   git clone https://github.com/MAM-debug/Python-Projects.git
   cd Python-Projects
   ```

2. **Navigate to the project folder** you want to run
   ```bash
   cd Streamlit
   ```

3. **Read the project's README** for specific instructions
   ```bash
   cat README.md
   ```

4. **Install dependencies** (if needed)
   ```bash
   # For Weather App
   pip install streamlit requests
   
   # For CSV Explorer
   pip install streamlit pandas
   ```

5. **Run the Python file**
   ```bash
   python filename.py
   # or for Streamlit apps:
   streamlit run filename.py
   ```

6. **Follow the on-screen prompts**

---

## Learning Path

| Project | Level | Time | What You Learn |
|---------|-------|------|-----------------|
| Quiz Game | 🟢 Beginner | 30 min | Variables, Loops, Conditionals |
| Number Guessing | 🟢 Beginner | 30 min | Functions, Input, Logic |
| Weather App | 🟡 Intermediate | 2 hours | APIs, Web Frameworks, Libraries |
| CSV Explorer | 🟡 Intermediate | 1 hour | Data Analysis, Pandas, File Handling |

---

## Contributions
Feel free to:
- 🍴 Fork this repository
- 🐛 Report bugs
- ✨ Suggest improvements
- 📝 Add new projects

---

## License
Free to use for learning purposes - MIT License

---

## Author
Created by [@MAM-debug](https://github.com/MAM-debug)

---

**Happy Learning! 🚀**

Remember: Every expert was once a beginner. Keep coding! 💪
