import random

word_list = [
	"apple", "grape", "mango", "plumb", "lemon", "peach", "melon", "pears", "citrus", "papay", "berry", "bacon", "bread", "bagel", "beans", "olive", "salad", "happy", "lucky", "peace", "shame", "shock", "worry", "cheer", "gloom", "panic", "anger", "angry", "green", "world",  "music", "piano", "cloud", "light", "night", "house", "river", "flame", "stone", "shoes", "chair", "table", "plant", "route", "crash", "clown", "shaky", "vegan", "power", "trust", "enjoy", "brick", "glent", "jumpy","trace", "ratio", "stain", "toast", "stare", "tales", "clock", "place"
	] 


def choose_word():
    return random.choice(word_list).lower()


def check_guess(word, guess):
	feedback = []
	word_chars = list(word)
	for i in range(len(word)):
		if guess[i] == word[i]:
			feedback.append((guess[i].upper(), "✅"))
			word_chars[i] = None
		else:
			feedback.append((guess[i], None))
	for i in range(len(word)):
		if feedback[i][1] is None: 
			if guess[i] in word_chars and guess[i] != word[i]:
				feedback[i] = (guess[i].upper(),"🌕")
				word_chars[word_chars.index(guess[i])] = None
	for i in range(len(word)):
		if feedback[i][1] is None:
			feedback[i] = (guess[i].upper(),"⬜")
	response_string = ""
	for letter in feedback:
		response_string += letter[0] + "  " + letter[1] + "  "
	return response_string

print("Welcome to the Wordle!")
print("You have 6 Attempts to guess the word!💪")
print("Note: ✅  stands for the correct letter and placement, 🌕  stands for the correct letter and wrong placement, and ⬜  stands for the wrong letter!")
play = True
streak = 0
while play: 
	target_word = choose_word()
	attempts = 6
	while True:
		if attempts == 0:
			print(f"Sorry, you ran out of attempts. The word was {target_word}")
			streak=0
			break
		user_guess = input("What is your Guess? ")
		while len(user_guess) != 5:
			user_guess = input("Sorry, your input is not valid! What is your Guess? ")
		user_guess_list = list(user_guess.lower())
		results = check_guess(target_word,user_guess_list)
		print(results)
		attempts -= 1
		if target_word == user_guess.lower():
			print(f"Congratulations! You guessed the word in {6-attempts} tries!")
			streak += 1
			break
		else:
			print(f"You have {attempts} Attempts left to guess the word!")
	print(f"Your current streak is {streak}!")
	play_again = input("Would you like to play again? Type 'y' for yes and 'n' for no: ")
	if play_again.lower() == "n" or play_again.lower() == "no":
		print("Thank you for playing the Wordle!")
		play = False
