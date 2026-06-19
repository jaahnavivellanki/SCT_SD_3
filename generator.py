"""
Sudoku Puzzle Generator Module.
Produces valid randomized puzzles with varying difficulties, guaranteeing unique solutions.
"""

import random
import copy
from sudoku_solver import SudokuSolver
from utils import create_empty_board


class SudokuGenerator:
    """
    Handles the generation of complete and partial Sudoku grids.
    """

    def __init__(self):
        """Initializes the generator with a solver instance."""
        self.solver = SudokuSolver()

    def generate(self, difficulty="Medium"):
        """
        Generates a valid randomized Sudoku puzzle with a unique solution.

        Args:
            difficulty (str): "Easy", "Medium", or "Hard".

        Returns:
            list[list[int]]: 9x9 Sudoku grid with cells removed based on difficulty.
        """
        board = create_empty_board()
        self._fill_diagonal_boxes(board)

        # Fill the rest of the board using the solver to ensure validity
        self.solver.solve(board)

        cells_to_remove = self._get_removal_count(difficulty)
        self._remove_cells_unique(board, cells_to_remove)

        return board

    def _fill_diagonal_boxes(self, board):
        """
        Fills the 3 diagonal 3x3 boxes with random numbers.
        They are independent of each other, allowing for safe random placement.
        """
        for i in range(0, 9, 3):
            self._fill_box(board, i, i)

    def _fill_box(self, board, row_start, col_start):
        """Fills a 3x3 box with numbers 1-9 in randomized order."""
        nums = list(range(1, 10))
        random.shuffle(nums)
        index = 0
        for i in range(3):
            for j in range(3):
                board[row_start + i][col_start + j] = nums[index]
                index += 1

    def _get_removal_count(self, difficulty):
        """Returns the number of cells to remove based on difficulty."""
        difficulty = difficulty.capitalize()
        if difficulty == "Easy":
            return random.randint(30, 38)
        elif difficulty == "Medium":
            return random.randint(40, 48)
        elif difficulty == "Hard":
            return random.randint(50, 58)
        return 40  # Default to Medium

    def _count_solutions(self, board):
        """
        Counts the number of valid solutions for a given board (up to 2).
        Used to guarantee uniqueness of the generated puzzle.
        """
        solutions = 0

        def solve_recursive(b):
            nonlocal solutions
            if solutions > 1:
                return True
            empty = self.solver.find_empty_cell(b)
            if not empty:
                solutions += 1
                return False
            row, col = empty
            for num in range(1, 10):
                if self.solver.is_valid(b, row, col, num):
                    b[row][col] = num
                    solve_recursive(b)
                    b[row][col] = 0
            return False

        solve_recursive(copy.deepcopy(board))
        return solutions

    def _remove_cells_unique(self, board, count):
        """
        Randomly removes a specific number of cells from the grid while
        ensuring the puzzle maintains exactly one unique solution.
        """
        cells = [(row, col) for row in range(9) for col in range(9)]
        random.shuffle(cells)
        
        cells_removed = 0
        for row, col in cells:
            if cells_removed >= count:
                break
                
            backup = board[row][col]
            board[row][col] = 0
            
            # Check if removing this cell causes multiple solutions
            if self._count_solutions(board) != 1:
                # If not unique, put the number back
                board[row][col] = backup
            else:
                cells_removed += 1
