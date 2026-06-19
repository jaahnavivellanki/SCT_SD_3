"""
Professional Sudoku Solving Engine using Backtracking.
"""


class InvalidSudokuError(Exception):
    """Exception raised when a Sudoku grid contains invalid or conflicting numbers."""
    pass


class UnsolvableSudokuError(Exception):
    """Exception raised when a valid Sudoku puzzle has no solution."""
    pass


class SudokuSolver:
    """
    A professional Sudoku solver engine implementing the backtracking algorithm.
    Tracks performance statistics such as recursive calls and backtracks.
    """

    def __init__(self):
        """Initializes the solver and its statistics dictionary."""
        self.stats = {'recursive_calls': 0, 'backtracks': 0}

    def is_valid(self, board, row, col, num):
        """
        Determines if a number can be placed in a specific cell according to Sudoku rules.

        Args:
            board (list[list[int]]): The 9x9 Sudoku grid.
            row (int): The row index (0-8).
            col (int): The column index (0-8).
            num (int): The number to validate (1-9).

        Returns:
            bool: True if the placement is valid, False otherwise.
        """
        # Check row and column for duplicates
        for i in range(9):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False

        # Check the 3x3 subgrid for duplicates
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False

        return True

    def find_empty_cell(self, board):
        """
        Finds the first empty cell (represented by 0) in the grid.

        Args:
            board (list[list[int]]): The 9x9 Sudoku grid.

        Returns:
            tuple[int, int] | None: A tuple (row, col) if an empty cell is found,
                                    or None if the grid is completely filled.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return (row, col)
        return None

    def validate_board(self, board):
        """
        Validates the initial state of the grid to ensure no conflicting numbers exist.

        Args:
            board (list[list[int]]): The 9x9 Sudoku grid.

        Raises:
            ValueError: If the board dimensions are not 9x9.
            InvalidSudokuError: If the board contains rule-breaking numbers.
        """
        if not board or len(board) != 9 or any(len(row) != 9 for row in board):
            raise ValueError("Invalid board dimensions. Sudoku grid must be exactly 9x9.")

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != 0:
                    if not (1 <= num <= 9):
                        raise InvalidSudokuError(
                            f"Invalid number '{num}' at row {row + 1}, col {col + 1}. "
                            "Numbers must be between 1 and 9."
                        )

                    # Temporarily empty the cell to validate the number against the rest of the board
                    board[row][col] = 0
                    is_num_valid = self.is_valid(board, row, col, num)
                    board[row][col] = num  # Restore the number

                    if not is_num_valid:
                        raise InvalidSudokuError(
                            f"Invalid grid: Conflicting number '{num}' found at "
                            f"row {row + 1}, column {col + 1}."
                        )

    def _solve_recursive(self, board, step_callback=None):
        """
        Internal recursive function implementing the Backtracking algorithm.

        Args:
            board (list[list[int]]): The 9x9 Sudoku grid.
            step_callback (callable, optional): A function to call at each step for visualization.

        Returns:
            bool: True if a solution is found, False otherwise.
        """
        self.stats['recursive_calls'] += 1

        empty_cell = self.find_empty_cell(board)

        # Base case: if no empty cells are found, the puzzle is solved
        if not empty_cell:
            return True

        row, col = empty_cell

        for num in range(1, 10):
            if self.is_valid(board, row, col, num):
                board[row][col] = num
                if step_callback:
                    step_callback(row, col, num, False)

                # Recursively attempt to solve the rest of the board
                if self._solve_recursive(board, step_callback):
                    return True

                # Backtrack: if the placement doesn't lead to a solution, reset and try next number
                board[row][col] = 0
                self.stats['backtracks'] += 1
                if step_callback:
                    step_callback(row, col, 0, True)

        return False

    def solve(self, board, step_callback=None):
        """
        Solves the Sudoku puzzle in place.

        Args:
            board (list[list[int]]): The 9x9 Sudoku grid.
            step_callback (callable, optional): Function to call on placement/backtrack.

        Returns:
            bool: True if solved successfully.

        Raises:
            ValueError: If board dimensions are incorrect.
            InvalidSudokuError: If the initial board is malformed/invalid.
            UnsolvableSudokuError: If no valid solution exists.
        """
        self.stats = {'recursive_calls': 0, 'backtracks': 0}

        # Validate grid configuration before attempting to solve
        self.validate_board(board)

        # Start solving via recursive backtracking
        is_solved = self._solve_recursive(board, step_callback)

        if not is_solved:
            raise UnsolvableSudokuError("The provided Sudoku puzzle has no valid solution.")

        return True

    def validate_initial_board(self, board):
        """
        Wrapper for validate_board that returns a boolean instead of raising exceptions.
        Kept for backward compatibility.
        """
        try:
            self.validate_board(board)
            return True
        except (ValueError, InvalidSudokuError):
            return False
