import tkinter as tk
from tkinter import messagebox
class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="lightgreen")
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = 'X'
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[None] * 3 for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Helvetica", 20), width=5, height=2,
                                   bg="white", activebackground="lightgray",
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = button
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game, font=("Helvetica", 14))
        self.reset_button.grid(row=3, column=0, columnspan=3, pady=10)

    def on_button_click(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "Match draw!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] is not None:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return True
        return False

    def check_draw(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is None:
                    return False
        return True

    def disable_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)

    def reset_game(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = 'X'
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state=tk.NORMAL)
root = tk.Tk()
app = TicTacToeApp(root)
root.mainloop()