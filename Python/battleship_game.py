# battleship_game.py
# 2016-08-24, Michael Hannon
# A functioning Battleship game, with proper error handling.
# Unlike the traditional game, user only gets four tries before the game exits.

# Import modules
from random import randint

# Initialize board and fill the spaces in appropriately
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

# Start the game by printing out the board and welcoming the user
print "Let's play Battleship!"
print_board(board)

# Place the battleship on a random space within the board's limits
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# print ship_row -- Debugging only!  This will print out the ship's location on the board.
# print ship_col -- Debugging only!  This will print out the ship's location on the board.

# The main game.  Have the user input the row and column, then check whether it's the battleship or not.
# If the user sinks the battleship, exit the game.  If not, allow four guesses.
for turn in range(4):
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Column :"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not on the board."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already.  Try again!"
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "Game Over"
        else:
            print "Turn #", turn + 1
            print_board(board)
