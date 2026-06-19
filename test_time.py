import time
from generator import SudokuGenerator

gen = SudokuGenerator()

start = time.perf_counter()
board = gen.generate("Hard")
print(f"Time taken: {time.perf_counter() - start:.4f} seconds")
