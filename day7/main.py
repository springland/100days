
#step 1

word_list = ["aardvark", "baboon", "camel"]

lives = 6

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random
choosen_word = random.choice(word_list)

print(f"The word is {choosen_word}")
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.



#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for index in range(len(choosen_word)):
    display.append('_')

print(display)

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
hasWon = False

while not hasWon and lives > 0:
    guess = input("Guess a letter:").lower()

    if guess in choosen_word:
        for index in range(len(choosen_word)):
            ch = choosen_word[index]
            if ch == guess:
                display[index] = ch
        if "_" not in display:
            hasWon = True
    else:
        print(stages[lives-1])
        lives -= 1
    print(display)


if lives == 0:
    print("Game over")
else:
    print(" You have won")
