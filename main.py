from random_word import RandomWords

# Hangman
lives = 6
hangman_stages = [
'''
------
|    |
|    0
|   \\|/
|   / \\   
|
======
''',
'''
------
|    |
|    0
|   \\|/
|   /   
|
======
''',
'''
------
|    |
|    0
|   \\|/
|  
|
======
''',
'''
------
|    |
|    0
|   \\|
|  
|
======
''',
'''
------
|    |
|    0
|
|   
|
======
''',
'''
------
|    |
|
|
|
|
======
'''
]
# Choose a random word from the word_list
chosen_word = RandomWords().get_random_word()
# Create a list to represent the guessed word
guessed_word = ["_"] * len(chosen_word)

# Keep track of previous guesses
previous_guesses = []

while lives > 0 and "_" in guessed_word:
    # Grab the user's input
    guessed_letter = input("Guess a letter?")

    # Check if the letter has already been guessed
    if guessed_letter in previous_guesses:
        print("You've already guessed that letter.")
        continue

    previous_guesses.append(guessed_letter)

    if guessed_letter in chosen_word:
        correct_guess = False
        # Loop through the chosen word and put the correct word in the correct index
        for i in range(len(chosen_word)):
            if guessed_letter == chosen_word[i]:
                guessed_word[i] = guessed_letter
                correct_guess = True

        if correct_guess:
            print("Correct!")
        else:
            lives -= 1
            print("Incorrect!")
    else:
        lives -= 1
        print("Incorrect!")

    print(" ".join(guessed_word))
    print(f"Previous guesses: {', '.join(previous_guesses)}")
    print(f"Lives remaining: {lives}\n")
    if lives != 0:
        print(hangman_stages[lives - 1])

if lives == 0:
    print('''D. E. A. D. ''')
    print(hangman_stages[0])
    print(f"You lost, bozo - the word was {chosen_word}")
else:
    print("You won, but at what cost, how many limbs did you let go! HOW MANY!")
