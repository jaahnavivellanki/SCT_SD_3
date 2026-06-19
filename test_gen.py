from generator import SudokuGenerator
gen = SudokuGenerator()
successes = 0
for i in range(100):
    try:
        board = gen.generate("Easy")
        successes += 1
    except Exception as e:
        print(f"Failed at iteration {i}: {e}")
        import traceback
        traceback.print_exc()
        break
print(f"Successes: {successes}/100")
