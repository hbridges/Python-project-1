"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    print("Welcome to the guessing game good luck!")
    answer = random.randrange(11)
    count = 1

    while True:
        guess = input("Pick a number between 1 and 10  ")

        if int(guess) > answer:
            print("It's lower. ")
            count += 1
            continue
        if int(guess) < answer:
            print("It's higher.")
            count += 1
            continue
        if int(guess) == answer:
            print("Thats the number you won! It took you {} attempts".format(count))
            print("THE GAME IS OVER!")
            break

    """Psuedo-code Hints
    ( You can add more features/enhancements if you'd like to. )
    """


if __name__ == '__main__':
    start_game()
