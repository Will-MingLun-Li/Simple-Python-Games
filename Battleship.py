from random import randint

board = []

for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ("You have 10 guesses, good luck!")

for turn in range(10):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    print (" ")

    if guess_row == ship_row and guess_col == ship_col:
        print_board(board)
        print ("Congratulations! You sunk my battleship!")
        input("Press Enter to Continue")
        break
    else:
        if(turn == 9):
            board[ship_row][ship_col] = "H"
            print (turn + 1)
            print_board(board)
            if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
                print ("That's out of range!")
            elif (board[guess_row][guess_col] == "X"):
                print ("You guessed that one already!")
            else:
                print("You missed my battleship!")
            print ("Game Over")
            print ("The ship was at (%s,%s) as indicated by 'H'" %(ship_row, ship_col))
            print (" ")
            input("Press 'Enter' to Exit")
        elif (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
            print (turn + 1)
            print_board(board)
            print ("That's out of range!")
            print (" ")
        elif (board[guess_row][guess_col] == "X"):
            print (turn + 1)
            print_board(board)
            print ("You guessed that one already.")
            print (" ")
        else:
            board[guess_row][guess_col] = "X"
            print (turn + 1)
            print_board(board)
            print ("You missed my battleship!")
            print (" ")

            



