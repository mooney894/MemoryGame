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
        self.root.geometry("400x300")
        
        self.current_level = 1
        self.lives = NUM_LIVES
        self.numbers_to_remember = []
        self.user_numbers = []
        
        self.label = tk.Label(root, text="Memorise the numbers", font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.pack()

    # Create a function to generate random numbers for each level and section
    def generate_numbers(self):
        num_count = self.current_level + self.section + 2
        self.numbers_to_remember = random.sample(range(1, 100), num_count)
        

    # Create a function to display the numbers to the player
    def display_numbers(self):
        self.label.configure(text="Memorise the following numbers: ")
        self.root.update()
        time.sleep(3)
        self.label.configure(text="")
        self.root.update()
        
        # Display numbers in a separate label
        numbers_text = " ".join(str(num) for num in self.numbers_to_remember)
        numbers_label = tk.Label(self.root, text=numbers_text, font=("Arial", 24))
        numbers_label.pack(pady=10)
        self.root.update()
        time.sleep(2)
        numbers_label.destroy()
    
    # Create a function to get the player's input for each section
    def get_player_input(self):
        expected_count = self.current_level + self.section + 2
        self.label.configure(text=f"Enter the {expected_count} numbers you remember: ")
        self.root.update()
        
    def check_answer(self):
        if self.user_numbers == self.numbers_to_remember:
            messagebox.showinfo("Correct", "Correct!")
        else:
            messagebox.showerror("Incorrect", "Incorrect!")
            self.lives -= 1
            
            if self.lives == 0:
                messagebox.showinfo("Game Over", "Game Over!")
                self.root.destory()
            else:
                self.current_level -= 1
                
    def start_game(self):
        self.start_button.config(state="disabled")
        self.label.config(font=("Arial", 18))

        while self.current_level <= NUM_LEVELS and self.lives > 0:
            self.label.configure(text=f"Level {self.current_level}")
            self.root.update()
            time.sleep(2)

            for self.section in range(NUM_SECTIONS):
                self.generate_numbers()
                self.display_numbers()
                self.get_player_input()

                self.user_numbers.clear()

                self.entry = tk.Entry(root, font=("Arial", 18))
                self.entry.pack(pady=10)

                self.submit_button = tk.Button(root, text="Submit", command=self.submit_numbers)
                self.submit_button.pack()

                self.entry.focus_set()
                self.root.bind("<Return>", self.submit_numbers)

                self.root.wait_window()

                self.entry.destroy()
                self.submit_button.destroy()

                if self.lives == 0:
                    break

            self.current_level += 1

        if self.lives > 0:
            messagebox.showinfo("Congratulations", "Congratulations! You completed all levels.")
            
    def submit_numbers(self, event=None):
        user_input = self.entry.get().strip()
        self.user_numbers = list(map(int, user_input.split()))
        self.check_answer()
        self.root.focus_force()
        self.entry.delete(0, tk.END)
        
if __name__ == "__main__":
    root = tk.Tk()
    memory_game = MemoryGame(root)
    root.mainloop()