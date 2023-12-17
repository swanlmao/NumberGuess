import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x200")
        
        self.lower_limit = 1
        self.upper_limit = 100
        self.target_number = random.randint(self.lower_limit, self.upper_limit)
        self.attempts = 0
        
        self.label = tk.Label(master, text="Guess the number:", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack(pady=10)
        
        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
        
        self.guess_button = tk.Button(master, text="Submit Guess", font=("Arial", 12), command=self.check_guess)
        self.guess_button.pack(pady=10)
        
    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.attempts += 1
            
            if user_guess < self.target_number:
                self.result_label.config(text="Too low! Try again.")
            elif user_guess > self.target_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed the number {self.target_number} correctly in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
    
    def reset_game(self):
        self.target_number = random.randint(self.lower_limit, self.upper_limit)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()