import random
import tkinter as tk
from tkinter import messagebox

# Function for the console version
def console_version():
    number_to_guess = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        try:
            guess = int(input(f"Guess a number between 1 and 100 (Attempts remaining: {attempts}): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            break

        attempts -= 1

    if attempts == 0:
        print(f"Sorry, you're out of attempts! The number was {number_to_guess}.")

# Function for the GUI version
class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 10

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_guess)
        self.submit_button.pack()

        self.attempts_label = tk.Label(master, text=f"Attempts remaining: {self.attempts}")
        self.attempts_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
            return

        if guess < self.number_to_guess:
            messagebox.showinfo("Hint", "Too low! Try again.")
        elif guess > self.number_to_guess:
            messagebox.showinfo("Hint", "Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", "You guessed the number!")
            self.master.quit()

        self.attempts -= 1
        self.attempts_label.config(text=f"Attempts remaining: {self.attempts}")

        if self.attempts == 0:
            messagebox.showinfo("Game Over", f"Sorry, you're out of attempts! The number was {self.number_to_guess}.")
            self.master.quit()

# Main function to choose between console or GUI
def main():
    choice = input("Would you like to play in console (C) or GUI (G) mode? ").strip().lower()
    if choice == 'c':
        console_version()
    elif choice == 'g':
        root = tk.Tk()
        game = NumberGuessingGame(root)
        root.mainloop()
    else:
        print("Invalid choice. Please enter 'C' for console or 'G' for GUI.")

if __name__ == "__main__":
    main()
