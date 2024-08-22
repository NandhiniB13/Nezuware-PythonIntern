import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.configure(bg="#d3d3d3")
        self.user_score = 0
        self.computer_score = 0
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Rock, Paper, Scissors", font=("Helvetica", 16), bg="#d3d3d3")
        self.title_label.pack(pady=10)
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("rock"), bg="#f0f0f0")
        self.rock_button.pack(side=tk.LEFT, padx=20)
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("paper"), bg="#add8e6")
        self.paper_button.pack(side=tk.LEFT, padx=20)
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("scissors"), bg="#ffb6c1")
        self.scissors_button.pack(side=tk.LEFT, padx=20)
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#d3d3d3")
        self.result_label.pack(pady=10)
        self.score_label = tk.Label(self.root, text="Score: I  0 - 0 You", font=("Helvetica", 12), bg="#d3d3d3")
        self.score_label.pack(pady=10)
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_scores, bg="#f0f0f0")
        self.reset_button.pack(pady=10)

    def play(self, user_choice):
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        if user_choice == computer_choice:
            result = "tie"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "user"
            self.user_score += 1
        else:
            result = "computer"
            self.computer_score += 1
        self.result_label.config(text=f"I choose {user_choice}. You choose {computer_choice}.")
        if result == "tie":
            messagebox.showinfo("Result", "It's a tie!")
        elif result == "user":
            messagebox.showinfo("Result", "I win this round!")
        else:
            messagebox.showinfo("Result", "You wins this round!")
        self.score_label.config(text=f"Score: [ I score ({self.user_score}) - ({self.computer_score}) You score]")

    def reset_scores(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score: I am 0 - 0 You")
        self.result_label.config(text="")
root = tk.Tk()
app = RockPaperScissorsApp(root)
root.mainloop()


