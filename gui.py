"""
Modern Dark-Themed GUI module for the Sudoku Solver application using Tkinter.
"""

import time
import tkinter as tk
from tkinter import messagebox, ttk
from sudoku_solver import SudokuSolver, InvalidSudokuError, UnsolvableSudokuError
from utils import create_empty_board
from generator import SudokuGenerator


class ModernButton(tk.Button):
    """A custom Tkinter button with hover effects to mimic modern design."""

    def __init__(self, master, **kw):
        """Initializes a flat, stylable button with hover bindings."""
        self.default_bg = kw.pop('bg', '#3a3a3a')
        self.hover_bg = kw.pop('activebackground', '#505050')
        self.default_fg = kw.pop('fg', '#ffffff')

        kw['bg'] = self.default_bg
        kw['fg'] = self.default_fg
        kw['activebackground'] = self.hover_bg
        kw['activeforeground'] = self.default_fg
        kw['relief'] = 'flat'
        kw['bd'] = 0
        kw['cursor'] = 'hand2'
        kw['font'] = kw.get('font', ('Segoe UI', 10, 'bold'))

        super().__init__(master, **kw)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        """Handles mouse hover entry."""
        self['background'] = self.hover_bg

    def on_leave(self, e):
        """Handles mouse hover exit."""
        self['background'] = self.default_bg


class SudokuGUI:
    """
    The main Graphical User Interface class for the Sudoku Solver Pro.
    """

    def __init__(self, root):
        """Initializes the Tkinter window, theme, and underlying models."""
        self.root = root
        self.root.title("Sudoku Solver Pro")

        # Colors (Internship-level design, Catppuccin Mocha inspired)
        self.bg_color = "#1e1e2e"
        self.grid_bg = "#313244"
        self.cell_bg = "#45475a"
        self.text_color = "#ffffff"
        self.accent_color = "#4CAF50"
        self.error_color = "#f38ba8"
        self.info_color = "#89b4fa"
        self.fixed_color = "#a6e3a1"

        self.root.configure(bg=self.bg_color)

        # Application Icon
       # try:
        #    icon_img = tk.PhotoImage(file="icon.png")
         #   self.root.iconphoto(False, icon_img)
       # except Exception as e:
        #    print(f"Icon not found: {e}")

        # Center the window
        window_width = 520
        window_height = 760
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.root.resizable(False, False)

        # Internal state
        self.solver = SudokuSolver()
        self.generator = SudokuGenerator()
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.initial_board = create_empty_board()
        self.current_difficulty = "Custom"
        
        self.animation_enabled = tk.BooleanVar(value=True)
        self.difficulty_var = tk.StringVar(value="Medium")

        # UI Setup
        self._create_widgets()
        self._create_grid()
        self._create_buttons()

    def _create_widgets(self):
        """Creates the main frames, title, status label, and footer."""
        # Header Frame
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.pack(pady=(25, 10))

        title_label = tk.Label(
            header_frame, text="Sudoku Solver Pro",
            font=("Segoe UI", 28, "bold"),
            bg=self.bg_color, fg=self.text_color
        )
        title_label.pack()

        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(expand=True)

        # Grid container (Dark border)
        self.grid_frame = tk.Frame(self.main_frame, bg="#11111b", bd=2)
        self.grid_frame.pack(pady=10)

        # Status Label
        self.status_label = tk.Label(
            self.root, text="Ready",
            font=("Segoe UI", 12, "bold"),
            bg=self.bg_color, fg=self.text_color
        )
        self.status_label.pack(pady=(5, 5))

        self.button_frame = tk.Frame(self.root, bg=self.bg_color)
        self.button_frame.pack(pady=10)

        # Footer Frame
        footer_frame = tk.Frame(self.root, bg=self.bg_color)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(0, 15))

        footer_label = tk.Label(
            footer_frame, text="Developed by Jaahnavi Vellanki",
            font=("Segoe UI", 10, "italic"),
            bg=self.bg_color, fg=self.accent_color
        )
        footer_label.pack()

    def _create_grid(self):
        """Creates the 9x9 grid of entry widgets with thick borders for 3x3 subgrids."""
        validate_cmd = (self.root.register(self._validate_input), '%P')

        for i in range(9):
            for j in range(9):
                # Calculate padding to visually separate 3x3 boxes
                pad_bottom = 2 if (i + 1) % 3 == 0 and i < 8 else 1
                pad_right = 2 if (j + 1) % 3 == 0 and j < 8 else 1
                pad_top = 1 if i == 0 else 0
                pad_left = 1 if j == 0 else 0

                cell_container = tk.Frame(self.grid_frame, bg=self.grid_bg)
                cell_container.grid(
                    row=i, column=j,
                    padx=(pad_left, pad_right), pady=(pad_top, pad_bottom)
                )

                entry = tk.Entry(
                    cell_container, width=2,
                    font=("Segoe UI", 20, "bold"), justify="center", bd=0,
                    bg=self.cell_bg, fg=self.text_color,
                    insertbackground=self.text_color,
                    disabledbackground=self.cell_bg,
                    disabledforeground=self.fixed_color
                )
                entry.pack(padx=1, pady=1, ipadx=5, ipady=5)
                entry.config(validate="key", validatecommand=validate_cmd)

                self.cells[i][j] = entry

    def _create_buttons(self):
        """Creates modern control buttons and toggles."""
        # Helper for DRY button creation
        def make_btn(parent, text, cmd, bg, abg, row, col, span=1):
            btn = ModernButton(
                parent, text=text, command=cmd,
                bg=bg, activebackground=abg, width=12, pady=8
            )
            btn.grid(row=row, column=col, columnspan=span, padx=5, pady=5)
            return btn

        # Row 1
        make_btn(self.button_frame, "SOLVE", self.solve_puzzle, self.accent_color, "#45a049", 0, 0)
        make_btn(self.button_frame, "VALIDATE", self.validate_puzzle, "#FF9800", "#FB8C00", 0, 1)

        # Row 2 (Difficulty & Generate are custom packed)
        diff_frame = tk.Frame(self.button_frame, bg=self.bg_color)
        diff_frame.grid(row=1, column=0, padx=5, pady=5)

        ttk.Style().configure(
            'TCombobox', fieldbackground=self.cell_bg,
            background=self.grid_bg, foreground="black"
        )
        diff_combo = ttk.Combobox(
            diff_frame, textvariable=self.difficulty_var,
            values=["Easy", "Medium", "Hard"],
            state="readonly", width=10, font=("Segoe UI", 10)
        )
        diff_combo.pack(side=tk.TOP)

        btn_generate = ModernButton(
            diff_frame, text="GENERATE", command=self.generate_puzzle,
            bg="#2196F3", activebackground="#1e88e5", width=12, pady=2
        )
        btn_generate.pack(side=tk.BOTTOM, pady=(2, 0))

        make_btn(self.button_frame, "RESET", self.reset_board, "#3a3a3a", "#505050", 1, 1)

        # Row 3
        make_btn(self.button_frame, "CLEAR", self.clear_board, "#3a3a3a", "#505050", 2, 0, span=2)

        # Row 4 for Animation Toggle
        anim_check = tk.Checkbutton(
            self.button_frame, text="Enable Solving Animation",
            variable=self.animation_enabled,
            bg=self.bg_color, fg=self.text_color,
            selectcolor=self.grid_bg, activebackground=self.bg_color,
            activeforeground=self.text_color, font=("Segoe UI", 10)
        )
        anim_check.grid(row=3, column=0, columnspan=2, pady=(10, 0))

    def _validate_input(self, text):
        """Validates that the input in entry fields is a single digit from 1 to 9 or empty."""
        if text == "":
            return True
        if len(text) == 1 and text.isdigit() and text != "0":
            return True
        return False

    def get_board(self):
        """Retrieves the current state of the grid and returns it as a 2D integer array."""
        board = create_empty_board()
        for i in range(9):
            for j in range(9):
                val = self.cells[i][j].get()
                board[i][j] = int(val) if val else 0
        return board

    def set_board(self, board, disable_initial=False, is_solved_overlay=False):
        """Updates the GUI grid with the values from the provided 2D array."""
        for i in range(9):
            for j in range(9):
                self.cells[i][j].config(bg=self.cell_bg)
                current_state = self.cells[i][j].cget("state")

                if current_state != "disabled":
                    self.cells[i][j].delete(0, tk.END)
                    if board[i][j] != 0:
                        self.cells[i][j].insert(0, str(board[i][j]))
                        if disable_initial:
                            self.cells[i][j].config(state="disabled")
                        elif is_solved_overlay:
                            self.cells[i][j].config(fg=self.accent_color)
                    else:
                        self.cells[i][j].config(state="normal", fg=self.text_color)

    def display_message(self, text, color):
        """Helper to update the main status label text and color."""
        self.status_label.config(text=text, fg=color)

    def validate_puzzle(self):
        """Action handler to explicitly validate the puzzle without solving."""
        board = self.get_board()
        try:
            self.solver.validate_board(board)
            messagebox.showinfo("Validation Passed", "The puzzle state is perfectly valid!")
            self.display_message("Puzzle Valid", self.accent_color)
        except InvalidSudokuError as e:
            messagebox.showerror("Validation Failed", str(e))
            self.display_message("Invalid Puzzle", self.error_color)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.display_message("Error", self.error_color)

    def visualize_step(self, row, col, num, is_backtrack):
        """Callback from solver to animate the backtracking process."""
        entry = self.cells[row][col]

        if is_backtrack:
            entry.config(bg=self.error_color)
            entry.delete(0, tk.END)
        else:
            entry.config(bg=self.accent_color)
            entry.delete(0, tk.END)
            entry.insert(0, str(num))

        self.root.update()
        time.sleep(0.02)  # Delay for smooth animation
        entry.config(bg=self.cell_bg)

    def solve_puzzle(self):
        """Action handler for the Solve button."""
        self.display_message("Solving...", self.info_color)
        self.root.update()

        board = self.get_board()
        callback = self.visualize_step if self.animation_enabled.get() else None

        try:
            start_time = time.perf_counter()
            if self.solver.solve(board, step_callback=callback):
                time_taken = time.perf_counter() - start_time

                self.set_board(board, is_solved_overlay=True)
                self.display_message("Puzzle Solved!", self.accent_color)

                stats = getattr(self.solver, 'stats', {'recursive_calls': 0, 'backtracks': 0})
                stats_msg = (
                    f"Difficulty: {self.current_difficulty}\n"
                    f"Time Taken: {time_taken:.4f} seconds\n"
                    f"Recursive Calls: {stats.get('recursive_calls', 0)}\n"
                    f"Backtracks: {stats.get('backtracks', 0)}"
                )
                messagebox.showinfo("Solve Statistics", stats_msg)

        except InvalidSudokuError as e:
            messagebox.showerror("Invalid Puzzle", str(e))
            self.display_message("Invalid Puzzle", self.error_color)
        except UnsolvableSudokuError as e:
            messagebox.showerror("No Solution", str(e))
            self.display_message("No Solution Exists", self.error_color)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.display_message("Error", self.error_color)

    def clear_board(self):
        """Action handler for the Clear button. Empties the grid completely."""
        self.initial_board = create_empty_board()
        self.current_difficulty = "Custom"
        for i in range(9):
            for j in range(9):
                self.cells[i][j].config(state="normal", fg=self.text_color, bg=self.cell_bg)
                self.cells[i][j].delete(0, tk.END)
        self.display_message("Board Cleared", self.text_color)

    def reset_board(self):
        """Action handler for the Reset button. Returns board to its initial generated state."""
        for i in range(9):
            for j in range(9):
                self.cells[i][j].config(state="normal", fg=self.text_color, bg=self.cell_bg)
                self.cells[i][j].delete(0, tk.END)

        self.set_board(self.initial_board, disable_initial=True)
        self.display_message("Board Reset", self.text_color)

    def generate_puzzle(self):
        """Action handler to generate a random puzzle based on difficulty dropdown."""
        self.clear_board()
        self.display_message("Generating...", self.info_color)
        self.root.update()

        difficulty = self.difficulty_var.get()
        new_board = self.generator.generate(difficulty)

        self.initial_board = [row[:] for row in new_board]  # deep copy
        self.set_board(new_board, disable_initial=True)
        self.current_difficulty = difficulty
        self.display_message(f"{difficulty} Puzzle Generated", self.info_color)
