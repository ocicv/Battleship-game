import random

def print_board(board):
    """
    Print the current state of the game board with labeled columns (numbers) and rows (letters).
    """
    print("   " + " ".join(str(i) for i in range(1, len(board) + 1)))
    for i, row in enumerate(board, start=1):
        print(f"{chr(64 + i)} | {' '.join(row)}")

def user_place_ship(board, ship_symbol):
    """
    Allow the user to choose a position for placing a ship on the board.
    """
    while True:
        try:
            ship_row = ord(input(f"Choose the row for your {ship_symbol} (A-J): ").upper()) - 65
            ship_col = int(input(f"Choose the column for your {ship_symbol}: ")) - 1

            if 0 <= ship_row < len(board) and 0 <= ship_col < len(board[0]) and board[ship_row][ship_col] == "O":
                board[ship_row][ship_col] = ship_symbol
                return ship_row, ship_col
            else:
                print("Invalid position. Please choose a valid and empty position.")
        except ValueError:
            print("Please input just one number")

def random_row_col(board):
    """
    Generate a random row or column index within the board size.
    """
    return random.randint(0, len(board) - 1)

def computer_place_ship(board, ship_symbol):
    """
    Place a computer ship at a random location on the board and return its coordinates.
    """
    ship_row, ship_col = random_row_col(board), random_row_col(board)

    while board[ship_row][ship_col] != "O":
        ship_row, ship_col = random_row_col(board), random_row_col(board)

    board[ship_row][ship_col] = ship_symbol
    return ship_row, ship_col

def user_guess(board):
    """
    Allow the user to guess a position on the board.
    """
    while True:
        try:
            guess_row = ord(input("Guess Row (A-J): ").upper()) - 65
            guess_col = int(input("Guess Column: ")) - 1

            if 0 <= guess_row < len(board) and 0 <= guess_col < len(board[0]):
                return guess_row, guess_col
            else:
                print(f"Please input valid letters (A-J) for rows and numbers between 1 and {len(board)} for columns.")
        except ValueError:
            print("Please input just one number")

def play_battleship():
    """
    Main function to orchestrate the Battleship game.
    """
    board_size = 10
    board = [["O"] * board_size for _ in range(board_size)]

    print("Let's play Battleship!")
    print_board(board)

    # User places their ships
    user_ships = []
    for i in range(3):
        print(f"\nPlace your ship {i + 1}")
        user_ship_row, user_ship_col = user_place_ship(board, "U")
        user_ships.append((user_ship_row, user_ship_col))

    # Computer places its ships
    computer_ships = []
    for i in range(3):
        computer_ship_row, computer_ship_col = computer_place_ship(board, "C")
        computer_ships.append((computer_ship_row, computer_ship_col))

    for turn in range(15):  # 15 turns total (adjust as needed)
        print(f"\nTurn {turn + 1}")

        # User's turn
        user_guess_row, user_guess_col = user_guess(board)
        for ship_row, ship_col in computer_ships:
            if user_guess_row == ship_row and user_guess_col == ship_col:
                print("Congratulations! You hit the computer's ship!")
                computer_ships.remove((ship_row, ship_col))
                break
        else:
            print("You missed!")

        # Computer's turn
        computer_guess_row, computer_guess_col = random_row_col(board), random_row_col(board)
        print(f"Computer guesses Row {chr(65 + computer_guess_row)}, Col {computer_guess_col + 1}")
        for ship_row, ship_col in user_ships:
            if computer_guess_row == ship_row and computer_guess_col == ship_col:
                print("Oh no! The computer hit your ship!")
                user_ships.remove((ship_row, ship_col))
                break
        else:
            print("Computer missed!")

        # Check for a winner
        if not user_ships:
            print("\nCongratulations! You sunk all of the computer's ships. You win!")
            break
        elif not computer_ships:
            print("\nOh no! The computer sunk all of your ships. You lose!")
            break

    print("\nGame Over.")
    print("Your remaining ships are at:")
    for ship_row, ship_col in user_ships:
        print(f"Row {chr(65 + ship_row)}, Col {ship_col + 1}")
    print("Computer's remaining ships are at:")
    for ship_row, ship_col in computer_ships:
        print(f"Row {chr(65 + ship_row)}, Col {ship_col + 1}")

if __name__ == "__main__":
    play_battleship()