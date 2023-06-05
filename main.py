# Import the required modules
import random
import time
import tkinter as tk
from tkinter import messagebox

# Define the constants for the game
NUM_LIVES = 3
NUM_LEVELS = 5
NUM_SECTIONS = 5

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        self.root.geometry("400x300")  # Adjust the window size here

        self.current_level = 1
        self.lives = NUM_LIVES
        self.number_to_remember = None
        self.user_number = None

        self.label = tk.Label(root, text="Memorize the number", font=("Arial", 24))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", font=("Arial", 18), command=self.start_game)
        self.start_button.pack()

    def generate_number(self):
        self.number_to_remember = random.randint(100, 999)

    def display_number(self):
        self.label.configure(text=f"Memorize the number: {self.number_to_remember}")
        self.root.update()
        time.sleep(3)
        self.label.configure(text="")
        self.root.update()

    def check_answer(self):
        if str(self.user_number.get()) == str(self.number_to_remember):
            messagebox.showinfo("Correct", "Correct!")

            if self.current_level == NUM_LEVELS:
                messagebox.showinfo("Game Over", "Congratulations! You completed all levels!")
                self.root.destroy()
            else:
                self.current_level += 1
                self.next_round()  # Call next_round to generate a new number
        else:
            messagebox.showerror("Incorrect", "Incorrect!")
            self.lives -= 1

            if self.lives == 0:
                messagebox.showinfo("Game Over", "Game over!")
                self.root.destroy()
            else:
                self.current_level -= 1

    def start_game(self):
        self.start_button.config(state="disabled")
        self.label.config(font=("Arial", 18))

        self.next_round()  # Call next_round to generate and display initial number

        for self.section in range(NUM_SECTIONS):
            self.user_number = tk.StringVar()

            self.entry = tk.Entry(root, font=("Arial", 18), textvariable=self.user_number)
            self.entry.pack(pady=10)

            self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
            self.submit_button.pack()

            self.entry.focus_set()
            self.root.bind("<Return>", self.check_answer)

            self.root.wait_window()

            self.entry.destroy()
            self.submit_button.destroy()

        if self.lives > 0:
            messagebox.showinfo("Game Over", "Game over!")

    def next_round(self):
        self.generate_number()
        self.display_number()
        
if __name__ == "__main__":
    root = tk.Tk()
    memory_game = MemoryGame(root)
    root.mainloop()