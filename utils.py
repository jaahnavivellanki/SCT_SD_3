"""
Utility module containing helper functions for the Sudoku Solver application.
Provides functions for generating empty grids.
"""


def create_empty_board():
    """
    Creates and returns a 9x9 empty Sudoku board filled with zeros.

    Returns:
        list[list[int]]: A 9x9 grid initialized with 0s.
    """
    return [[0 for _ in range(9)] for _ in range(9)]
