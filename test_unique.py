import copy
from sudoku_solver import SudokuSolver
from generator import SudokuGenerator

def count_solutions(board, solver):
    solutions = 0
    
    def solve_recursive(b):
        nonlocal solutions
        if solutions > 1: return True
        empty = solver.find_empty_cell(b)
        if not empty:
            solutions += 1
            return False
        row, col = empty
        for num in range(1, 10):
            if solver.is_valid(b, row, col, num):
                b[row][col] = num
                solve_recursive(b)
                b[row][col] = 0
        return False
        
    solve_recursive(copy.deepcopy(board))
    return solutions

gen = SudokuGenerator()
solver = SudokuSolver()
b = gen.generate("Easy")
print("Solutions:", count_solutions(b, solver))
