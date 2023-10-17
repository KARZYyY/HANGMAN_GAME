#BY KARZY

import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word_list = ["python", "java", "javascript", "html", "css", "ruby", "react", "angular", "django", "flask"]
        self.secret_word = random.choice(self.word_list)
        self.guess_word = ["_"] * len(self.secret_word)

        self.attempts = 6
        self.hangman_parts = 0

        self.word_label = tk.Label(root, text=" ".join(self.guess_word), font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.entry_label = tk.Label(root, text="Enter a letter:")
        self.entry_label.pack()

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var, font=("Helvetica", 18))
        self.entry.pack()

        self.guess_button = tk.Button(root, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=10)

        self.canvas = tk.Canvas(root, width=200, height=200)
        self.canvas.pack()

    def make_guess(self):
        guess = self.entry_var.get().lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in self.secret_word:
                for i in range(len(self.secret_word)):
                    if self.secret_word[i] == guess:
                        self.guess_word[i] = guess
            else:
                self.attempts -= 1
                self.draw_hangman()

            self.update_display()

            if "_" not in self.guess_word:
                messagebox.showinfo("Congratulations!", "You guessed the word!")
                self.restart_game()

            if self.attempts == 0:
                messagebox.showinfo("Game Over", f"You ran out of attempts. The word was {self.secret_word}.")
                self.restart_game()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")

    def update_display(self):
        self.word_label.config(text=" ".join(self.guess_word))
        self.entry_var.set("")
        self.entry.focus_set()

    def draw_hangman(self):
        parts = [
            (self.draw_head, (100, 40)),
            (self.draw_body, (100, 90)),
            (self.draw_left_leg, (80, 130)),
            (self.draw_right_leg, (120, 130)),
            (self.draw_left_arm, (80, 70)),
            (self.draw_right_arm, (120, 70))
        ]

        if self.hangman_parts < len(parts):
            draw_function, position = parts[self.hangman_parts]
            draw_function(*position)
            self.hangman_parts += 1

    def draw_head(self, x, y):
        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, width=2)

    def draw_body(self, x, y):
        self.canvas.create_line(x, y - 20, x, y + 60, width=2)

    def draw_left_leg(self, x, y):
        self.canvas.create_line(x, y, x - 30, y + 40, width=2)

    def draw_right_leg(self, x, y):
        self.canvas.create_line(x, y, x + 30, y + 40, width=2)

    def draw_left_arm(self, x, y):
        self.canvas.create_line(x, y, x - 20, y + 20, width=2)

    def draw_right_arm(self, x, y):
        self.canvas.create_line(x, y, x + 20, y + 20, width=2)

    def restart_game(self):
        self.secret_word = random.choice(self.word_list)
        self.guess_word = ["_"] * len(self.secret_word)
        self.attempts = 6
        self.hangman_parts = 0
        self.canvas.delete("all")  # Clear the canvas
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
