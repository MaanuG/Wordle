import random
import tkinter as tk
from tkinter import messagebox

# Custom list of easy 5-letter words
word_list = [
    "apple", "grape", "peach", "lemon", "plumb", "chair", "table", "plant",
    "paper", "house", "river", "flame", "stone", "shoes", "bread", "night",
    "light", "green", "happy", "lucky", "world", "music", "piano", "cloud"
]

def choose_word():
    return random.choice(word_list).lower()

# ANSI color codes (we'll use tkinter labels to display colors)
GREEN = "#32CD32"  # Light Green
BRIGHT_YELLOW = "#FFFF00"  # Brighter Yellow
WHITE = "#FFFFFF"  # White (default)

# Function to check the guess and return feedback
def check_guess(word, guess):
    feedback = []
    word_chars = list(word)  # List of characters from the word to track used letters

    # First pass: Check for correct letters in the correct position (Green)
    for i in range(len(word)):
        if guess[i] == word[i]:
            feedback.append((guess[i].upper(), GREEN))
            word_chars[i] = None  # Remove the matched letter from word_chars to prevent reuse
        else:
            feedback.append((guess[i], None))

    # Second pass: Check for correct letters in the wrong position (Bright Yellow)
    for i in range(len(word)):
        if feedback[i][1] is None:  # Only process letters that haven't already been matched (Green)
            if guess[i] in word_chars and guess[i] != word[i]:
                feedback[i] = (guess[i], BRIGHT_YELLOW)
                word_chars[word_chars.index(guess[i])] = None  # Remove the matched letter from word_chars

    # Remaining letters are incorrect (White)
    for i in range(len(word)):
        if feedback[i][1] is None:
            feedback[i] = (guess[i], WHITE)

    return feedback

# Function to handle the gameplay in the tkinter window
class WordleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle Game")

        # Set up the game
        self.word = choose_word()
        self.attempts = 6
        self.guesses = []

        # Create the tkinter widgets
        self.create_widgets()

    def create_widgets(self):
        # Entry box for user guess (with customized font)
        self.entry_label = tk.Label(self.root, text="Enter a 5-letter guess:", font=("Courier New", 14, "bold"))
        self.entry_label.pack(pady=5)

        self.entry = tk.Entry(self.root, font=("Courier New", 14), width=20)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.submit_guess, font=("Courier New", 12), width=20)
        self.submit_button.pack(pady=10)

        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.attempts}", font=("Courier New", 12))
        self.attempts_label.pack(pady=10)

        # Frame for guesses (using a Frame widget to hold guesses in order)
        self.guesses_frame = tk.Frame(self.root)
        self.guesses_frame.pack(pady=10)

    def submit_guess(self):
        guess = self.entry.get().lower()
        if len(guess) != 5:
            messagebox.showwarning("Invalid Input", "Please enter a valid 5-letter word.")
            return

        # Check if the guess is correct
        if guess == self.word:
            feedback = check_guess(self.word, guess)
            self.attempts -= 1
            self.update_game(guess, feedback)

            # Show the correct message after updating the UI
            messagebox.showinfo("Congratulations!", f"Correct! The word was '{self.word}'")
            self.root.quit()
            return

        # Check guess and display feedback
        feedback = check_guess(self.word, guess)
        self.attempts -= 1
        self.update_game(guess, feedback)

        if self.attempts == 0:
            messagebox.showinfo("Game Over", f"Out of attempts! The word was '{self.word}'")
            self.root.quit()

    def update_game(self, guess, feedback):
        # Update attempts label
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

        # Create the guess label with feedback colors
        guess_feedback = ""
        for char, color in feedback:
            guess_feedback += char.upper()

        # Create a frame for the new guess
        guess_row = tk.Frame(self.guesses_frame)
        guess_row.pack(side="top", fill="x", pady=5)

        # Add each letter to the guess row
        for i, (char, color) in enumerate(feedback):
            label = tk.Label(guess_row, text=char.upper(), font=("Courier New", 14), bg=color, width=4, height=2, relief="solid")
            label.pack(side="left", padx=5)

        # Clear the entry box for the next guess
        self.entry.delete(0, tk.END)

# Main function to start the tkinter game
def main():
    root = tk.Tk()
    game = WordleGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
