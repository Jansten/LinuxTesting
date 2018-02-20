# while_loop_guess_number.py
# 2016-08-25, Michael Hannon
# Generates a random number, then uses a while loop to ask the user to guess the number.
# Code is based on a CodeCademy Python course

from random import randint

random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You Win!"
        break
    else:
        guesses_left -= 1
else:
    print "You lose."