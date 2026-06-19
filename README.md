# Sudoku Solver Pro 🧩

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

A professional, high-performance Sudoku Solver and Generator built entirely in Python. This project features a beautiful modern dark-themed graphical user interface, animated backtracking algorithms, and robust random puzzle generation. 

Designed and developed by **Jaahnavi Vellanki**.

---

## 🌟 Features

- **Blazing Fast Solving Engine**: Utilizes an optimized recursive backtracking algorithm to solve any valid 9x9 Sudoku puzzle instantly.
- **Random Puzzle Generator**: Automatically generate valid, randomized Sudoku puzzles across three difficulties: **Easy**, **Medium**, and **Hard**.
- **Solving Visualizer (Animation)**: Watch the computer solve the puzzle in real-time! The grid dynamically highlights successful forward placements in green, and red when it encounters a dead-end and is forced to backtrack.
- **Strict Validation**: The engine meticulously prevents mathematically conflicting numbers and raises intuitive custom exceptions/popups.
- **Detailed Statistics**: Curious about algorithm efficiency? The application tracks and displays exact microsecond compute times, total recursive calls, and total backtracks upon successfully solving a board.
- **Modern UI**: Polished using a premium Catppuccin Mocha-inspired dark theme, featuring flat hover-reactive buttons, crisp UI spacing, and a clean professional aesthetic.

---

## 📁 Project Structure

```text
SudokuSolverPro/
│
├── main.py               # Main application entry point
├── gui.py                # Modern Tkinter Graphical User Interface
├── sudoku_solver.py      # Core Backtracking Algorithm & Validation Engine
├── generator.py          # Difficulty-scaled Random Puzzle Generator
├── utils.py              # Utility functions for board management
├── icon.png              # Application Icon asset
├── requirements.txt      # Project dependencies
└── README.md             # This file
```

---

## 🚀 Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/SudokuSolverPro.git
   cd SudokuSolverPro
   ```

2. **Verify Python Installation**:
   Ensure you have Python 3.9 or newer installed. This application uses `tkinter` which is bundled with standard Python distributions. No external pip libraries are required!
   ```bash
   python --version
   ```

3. **Run the Application**:
   ```bash
   python main.py
   ```

---

## 📖 Usage Guide

### 1. Generating a Puzzle
Select your desired difficulty (**Easy, Medium, or Hard**) from the dropdown menu and click **GENERATE**. The board will be populated with a brand new, randomly generated Sudoku puzzle.

### 2. Manual Input
You can click on any cell in the 9x9 grid to input numbers manually. The fields are restricted to accept only a single digit from `1-9`.

### 3. Validating the Board
If you've entered numbers manually and want to check if the layout is mathematically sound without solving it, click **VALIDATE**. A popup will let you know if the grid is valid or if there are conflicting numbers in rows, columns, or 3x3 grids.

### 4. Solving the Puzzle
Click **SOLVE** to let the engine take over. 
- If **Enable Solving Animation** is checked, you will watch the backtracking visualization.
- If unchecked, the puzzle will be solved in milliseconds.

When the solution is found, a statistics popup will appear detailing the time taken, recursive calls, and the number of backtracks!

### 5. Managing the Board
- **RESET**: Reverts the board back to its original state (e.g., undoes the solver or your manual mistakes, bringing you back to the originally generated puzzle).
- **CLEAR**: Completely empties the grid, preparing it for a fresh manual input.
