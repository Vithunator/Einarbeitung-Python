from turtle import clear
import time
import os
from operator import truediv


def dominik():  # RandomNumberGuesser

    import random
    randomNumber = r.Next(0, 100)
    win = False
    counter = 0


def vithu():  # TicTacToe
    print("Vithu")
    return


# Main game:
while (True):
    print(
        "Willkommen zu unserer kleinen Projektesammlung!\n" +
        "Tippen Sie die Zahl neben einem Projekt ein,\n" +
        "um das jeweilige Projekt anzuschauen:\n\n" +
        "(1) Tic Tac Toe\n" +
        "(2) Random Number Guesser")

    userInput = int(input())

    if (userInput == 1):
        vithu()
    elif (userInput == 2):
        dominik()
    else:
        os.system('cls')
        print("\033[1;31;40m\n")
        print("Ein Fehler ist aufgetreten")
        time.sleep(1.5)
        print("\033[0;37;40m\n")
        os.system('cls')
        continue

    break
