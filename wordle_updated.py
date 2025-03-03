import random

word_list = [
    "apple", "grape", "peach", "lemon", "plumb", "chair", "table", "plant",
    "paper", "house", "river", "flame", "stone", "shoes", "bread", "night",
    "light", "green", "happy", "lucky", "world", "music", "piano", "cloud"
]

def choose_word():
    return random.choice(word_list).lower()

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

target_word = choose_word()
print("Welcome to the Wordle!")
print("You have 6 Attempts to guess the word!")
attempts = 6
while True:
    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The word was {target_word}")
        break
    user_guess = input("What is your Guess? ")
    user_guess_list = list(user_guess.lower())
    results = check_guess(target_word,user_guess_list)
    print(results)
    attempts -= 1
    if target_word == user_guess.lower():
        print(f"Congratulations! You guessed the word in {6-attempts} tries!")
        break
    else:
        print(f"You have {attempts} Attempts left to guess the word!")

