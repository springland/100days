
import random

from art import logo

HARD = 5
EASY = 10


def number_guessing():
    print(logo)
    print("Welcome to the number guessing game !")
    print("I'm thinking of a number between 1 and 100.")
    target = random.randint(1 , 100)
    difficulity = input("Choose a difficulity. Type 'easy' or 'hard' ").lower()
    if difficulity == 'easy':
        rounds_remaining = EASY
    else:
        rounds_remaining = HARD

    match = False

    while rounds_remaining > 0 and not match:
        print(f"You have {rounds_remaining} attempt remaing to guess")
        guess_value = int(input("Please make a guess:"))
        if guess_value < target:
            print("Too Low")
        elif guess_value > target:
            print("Too high")
        else:
            match = True
        rounds_remaining -=1
        if rounds_remaining > 0:
            print ("Please guess again")

    if match:
        print(f"You found the right number {target}")
    else:
        print(" You run out of rounds , good luck next time")


number_guessing()
