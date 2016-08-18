#Asks the user to guess a number between one and five, with the appropriate responses.

x = int(raw_input("What number am I thinking of between 1 and 5? "))

if x == 4:
    print('You guessed correctly!')
else:
    print('Wrong guess, try again!')

print('End of program.')