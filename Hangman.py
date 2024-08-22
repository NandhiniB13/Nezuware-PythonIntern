class HangmanGame:
    def __init__(self):
        self.word = ""
        self.guessed_letters = set()
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

    def set_word(self, word):
        if word.isalpha():
            self.word = word.lower()
            self.guessed_letters = set()
            self.attempts_left = self.max_attempts
            return True
        return False

    def make_guess(self, letter):
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("Invalid guess. Please enter a single letter.")
        letter = letter.lower()
        if letter in self.guessed_letters:
            return "already guessed"

        self.guessed_letters.add(letter)
        if letter in self.word:
            return "correct"
        else:
            self.attempts_left -= 1
            return "incorrect"

    def get_display_word(self):
        return ' '.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def is_won(self):
        return '_' not in self.get_display_word()

    def is_lost(self):
        return self.attempts_left <= 0
import tkinter as tk
from tkinter import simpledialog, messagebox
class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.game = HangmanGame()
        self.player1_name = ""
        self.player2_name = ""
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Hangman Game", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 20))
        self.word_label.pack(pady=10)
        self.attempts_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.attempts_label.pack(pady=10)
        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.guess_entry.pack(pady=10)
        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)
        self.setup_game()

    def setup_game(self):
        self.player1_name = simpledialog.askstring("Input", "Enter Player 1's name:")
        self.player2_name = simpledialog.askstring("Input", "Enter Player 2's name:")
        if not self.player1_name or not self.player2_name:
            messagebox.showerror("Error", "Both players must provide their names.")
            self.setup_game()
        else:
            self.reset_game()

    def reset_game(self):
        word = simpledialog.askstring(f"Input", f"{self.player1_name}, enter the word to guess:")
        if word and self.game.set_word(word):
            self.update_display()
        else:
            messagebox.showerror("Error", "Invalid word entered. Please enter a valid word.")
            self.reset_game()

    def make_guess(self):
        # Handle the player's guess
        guess = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)
        try:

            result = self.game.make_guess(guess)
            if result == "already guessed":
                messagebox.showinfo("Info", "You've already guessed that letter.")
            elif result == "correct":
                messagebox.showinfo("Correct", "Good guess!")
            else:
                messagebox.showinfo("Incorrect", "Wrong guess!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        self.update_display()
        if self.game.is_won():
            messagebox.showinfo("Congratulations!", f"{self.player2_name}, you've guessed the word!")
        elif self.game.is_lost():
            messagebox.showinfo("Game Over",
                                f"{self.player2_name}, you've run out of attempts. The word was '{self.game.word}'.")
    def update_display(self):

        display_word = self.game.get_display_word()
        self.word_label.config(text=display_word)
        self.attempts_label.config(text=f"Attempts left: {self.game.attempts_left}")
root = tk.Tk()
app = HangmanGUI(root)
root.mainloop()