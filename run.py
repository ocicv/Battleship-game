import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row_col(board):
    return random.randint(0, len(board) - 1)

def place_ship(board):
    ship_row = random_row_col(board)
    ship_col = random_row_col(board)
    board[ship_row][ship_col] = "S"
    return ship_row, ship_col

def user_guess(board):
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) - 1
    return guess_row, guess_col