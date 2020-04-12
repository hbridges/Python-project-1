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
    highscore = 100

    while True:
        try:
            guess = int(input("Pick a number between 1 and 10  "))
        except ValueError:
            print("Oops looks like you didn't enter a number")
            continue
        if guess < 1 or guess > 10:
            print("Please guess between 1 and 10 only")
            count += 1
            continue
        if guess > answer:
            print("It's lower. ")
            count += 1
            continue
        if guess < answer:
            print("It's higher.")
            count += 1
            continue
        if guess == answer:
            print("Thats the number you won! It took you {} attempts".format(count))
            print("THE GAME IS OVER!")
            replay = input(" Would you like to play again Y/N?  ")

            if replay.lower() == "y":
                if count <= highscore:
                    highscore = count
                print("The HIGHSCORE IS {}!".format(highscore))
                answer = random.randrange(11)
                count = 1
                continue

            break


if __name__ == '__main__':
    start_game()
