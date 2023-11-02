# Project made by Piotr Zięba on 31.10.2023. It is the number guessing game.
# It is 12th day of the bootcamp. The class is still related with beginner's level.
from art import logo
import random


def easy_game():
    # An easy level of the game. It gives the player 10 lives.
    lives = 10
    random_number = random.randint(0, 100)  # It selects a random number from given range.
    while lives > 0:    # Loops goes on for as long as the player has lives.
        choice = int(input(f"You have {lives} lives. Select a numer:"))
        if random_number < choice:    # Instructions for the player and final outcomes.
            lives -= 1
            print(f"Too high. You have {lives} lives left.")
        elif random_number > choice:
            lives -= 1
            print(f"Too low. You have {lives} lives left.")
        elif random_number == choice:
            print(f"You win! The right answer is {random_number}")
            break
        if lives == 0:
            print(f"Game over! The right answer is {random_number}")


def hard_game():
    # A hard version of the game. It gives the player 5 lives. Everything else is the same.
    lives = 5
    random_number = random.randint(0, 100)  # It selects a random number.
    while lives > 0:
        choice = int(input(f"You have {lives} lives. Select a numer:"))
        if random_number < choice:
            lives -= 1
            print(f"Too high. You have {lives} lives left.")
        elif random_number > choice:
            lives -= 1
            print(f"Too low. You have {lives} lives left.")
        elif random_number == choice:
            print(f"You win! The right answer is {random_number}")
            break
        if lives == 0:
            print(f"Game over! The right answer is {random_number}")


while True:    # Allows to play the game in a loop.
    print(logo)
    print("Welcome to the Number Guessing Game. It's time to have some fun!")
    print("Your task is to guess the number I've selected for you. Available range is from 0 to 100.")
    level = input("Choose difficulty. Type 'easy' or 'hard':")    # Here we select difficulty level.
    if level == "easy":    # Here we go for the right difficulty level.
        easy_game()
    elif level == "hard":
        hard_game()
    else:
        print("Wrong answer.")
