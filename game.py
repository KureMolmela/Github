# guessing game

from random import randint

number = randint(1, 5)
lives = 3

while lives > 0:
    choice = int(input("guess number: "))
    if choice == number:
        print("well done")
        break
    else:
        lives = lives - 1
