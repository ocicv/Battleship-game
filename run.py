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
    while True:
        try:
            guess_row = int(input("Guess Row: ")) - 1
            guess_col = int(input("Guess Col: ")) - 1

            # Check if the inputs are within the valid range
            if 0 <= guess_row < len(board) and 0 <= guess_col < len(board[0]):
                return guess_row, guess_col
            else:
                print("Please input valid numbers between 1 and", len(board))
        except ValueError:
            print("Please input just one number")

def play_battleship():
    board_size = 5
    board = [["O"] * board_size for _ in range(board_size)]

    print("Let's play Battleship!")
    print_board(board)

    user_ship_row, user_ship_col = place_ship(board)
    computer_ship_row, computer_ship_col = place_ship(board)

    for turn in range(5):  # You and the computer have 5 turns each
        print(f"\nTurn {turn + 1}")

        # User's turn
        user_guess_row, user_guess_col = user_guess(board)
        if user_guess_row == computer_ship_row and user_guess_col == computer_ship_col:
            print("Congratulations! You sunk the computer's battleship!")
            break
        else:
            print("You missed!")

        # Computer's turn
        computer_guess_row, computer_guess_col = random_row_col(board), random_row_col(board)
        print(f"Computer guesses Row {computer_guess_row + 1}, Col {computer_guess_col + 1}")
        if computer_guess_row == user_ship_row and computer_guess_col == user_ship_col:
            print("Oh no! The computer sunk your battleship!")
            break
        else:
            print("Computer missed!")

    print("\nGame Over.")
    print("Your battleship was at Row", user_ship_row + 1, "Col", user_ship_col + 1)
    print("Computer's battleship was at Row", computer_ship_row + 1, "Col", computer_ship_col + 1)

if __name__ == "__main__":
    play_battleship()