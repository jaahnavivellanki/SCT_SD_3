# Sudoku Solver Pro

A modern GUI-based Sudoku Solver developed using **Python** and **Tkinter**, implementing the **Backtracking Algorithm** to efficiently solve Sudoku puzzles. The application provides an intuitive interface for generating, validating, and solving Sudoku puzzles while demonstrating algorithmic problem-solving and software design principles.

---

## Overview

Sudoku Solver Pro is designed to automate the process of solving Sudoku puzzles through a structured and optimized backtracking approach. The project combines algorithmic efficiency with a user-friendly graphical interface, making it both functional and visually accessible.

---

## Features

* Interactive 9×9 Sudoku Board
* Automated Sudoku Solving
* Puzzle Validation and Error Detection
* Random Puzzle Generation
* Multiple Difficulty Levels
* Clear and Reset Functionality
* User-Friendly Graphical Interface
* Modular and Maintainable Code Structure
* Performance and Logic Testing

---

## Technology Stack

| Component               | Technology   |
| ----------------------- | ------------ |
| Programming Language    | Python       |
| GUI Framework           | Tkinter      |
| Algorithm               | Backtracking |
| Development Environment | VS Code      |
| Version Control         | Git & GitHub |

---

## Project Structure

```text
SCT_SD_3/
│
├── main.py              # Application entry point
├── gui.py               # Graphical User Interface
├── sudoku_solver.py     # Backtracking solver implementation
├── generator.py         # Puzzle generation logic
├── utils.py             # Utility functions
│
├── test_gen.py          # Generator testing
├── test_time.py         # Performance testing
├── test_unique.py       # Solution uniqueness testing
│
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## Algorithm

The application uses the **Backtracking Algorithm**, a recursive search technique that:

1. Finds an empty cell in the Sudoku grid.
2. Tries valid numbers from 1 to 9.
3. Verifies row, column, and sub-grid constraints.
4. Recursively continues until a solution is found.
5. Backtracks whenever a conflict occurs.

This approach guarantees a valid solution whenever one exists.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/jaahnavivellanki/SCT_SD_3.git
```

### Navigate to the Project Directory

```bash
cd SCT_SD_3
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Git Bash:

```bash
source venv/Scripts/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python main.py
```

---

## Key Learning Outcomes

* Object-Oriented Programming in Python
* GUI Development using Tkinter
* Recursive Problem Solving
* Backtracking Algorithms
* Software Testing and Validation
* Modular Application Design
* Version Control with Git and GitHub

---

## Future Enhancements

* Advanced Sudoku Generation
* Real-Time Solving Visualization
* Dark/Light Theme Support
* Hint System
* Save and Load Puzzle Functionality
* Performance Analytics Dashboard

---

## Author

**Jaahnavi Vellanki**
B.Tech – Information Technology

---

## License

This project is developed for educational and learning purposes.
