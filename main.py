"""
Main entry point for the Sudoku Solver Pro application.
"""
import tkinter as tk
from gui import SudokuGUI


def main():
    """
    Initializes the Tkinter window and starts the main application event loop.
    """
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
