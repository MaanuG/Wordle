import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

word_list = [
    "apple", "grape", "peach", "lemon", "plumb", "chair", "table", "plant",
    "paper", "house", "river", "flame", "stone", "shoes", "bread", "night",
    "light", "green", "happy", "lucky", "world", "music", "piano", "cloud"
]


def choose_word():
    return random.choice(word_list).lower()


# Color definitions (hex codes for internal mapping)
GREEN = "#32CD32"  # Light Green
BRIGHT_YELLOW = "#FFFF00"  # Brighter Yellow
WHITE = "#FFFFFF"  # White (default)


def check_guess(word, guess):
    feedback = []
    word_chars = list(word)  # List of characters from the word to track used letters

    # First pass: Check for correct letters in the correct position (Green)
    for i in range(len(word)):
        if guess[i] == word[i]:
            feedback.append((guess[i].upper(), GREEN))
            word_chars[i] = None  # Remove the matched letter to prevent reuse
        else:
            feedback.append((guess[i], None))

    # Second pass: Check for correct letters in the wrong position (Bright Yellow)
    for i in range(len(word)):
        if feedback[i][1] is None:  # Process only letters not already marked as green
            if guess[i] in word_chars and guess[i] != word[i]:
                feedback[i] = (guess[i].upper(), BRIGHT_YELLOW)
                word_chars[word_chars.index(guess[i])] = None  # Remove matched letter

    # Remaining letters are incorrect (White)
    for i in range(len(word)):
        if feedback[i][1] is None:
            feedback[i] = (guess[i].upper(), WHITE)

    return feedback


def display_feedback(feedback):
    # Map hex codes to colorama foreground colors
    color_mapping = {
        GREEN: Fore.GREEN,
        BRIGHT_YELLOW: Fore.YELLOW,
        WHITE: Fore.WHITE
    }
    for letter, color in feedback:
        # Default to reset if color not found
        color_code = color_mapping.get(color, Fore.RESET)
        print(color_code + letter + Style.RESET_ALL, end=" ")
    print()  # New line after printing all letters


target_word = choose_word()
print("Welcome to the Wordle!")
print(f"You have 6 attempts to guess the {len(target_word)}-letter word!")

attempts = 6
while True:
    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The word was '{target_word}'.")
        break
    user_guess = input("What is your Guess? ").lower()

    # Check if the guess has the correct length
    if len(user_guess) != len(target_word):
        print(f"Please enter a {len(target_word)}-letter word.")
        continue

    user_guess_list = list(user_guess)
    results = check_guess(target_word, user_guess_list)
    display_feedback(results)
    attempts -= 1

    if target_word == user_guess:
        print(f"Congratulations! You guessed the word in {6 - attempts} tries!")
        break
    else:
        print(f"You have {attempts} attempts left to guess the word!")
