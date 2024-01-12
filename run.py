import random
# Create boards for player
def create_board_computer():
    board = {
        '1A':' ', '2A':' ', '3A':' ', '4A':' ', '5A':' ',
        '1B':' ', '2B':' ', '3B':' ', '4B':' ', '5B':' ',
        '1C':' ', '2C':' ', '3C':' ', '4C':' ', '5C':' ',
        '1D':' ', '2D':' ', '3D':' ', '4D':' ', '5D':' ',
        '1E':' ', '2E':' ', '3E':' ', '4E':' ', '5E':' ',
        }
    ship_locs = random.sample(board.keys(), 6)
    for loc in ship_locs:
        board[loc] = 'O'
    return board

def create_board_player():
    board = {
        '1A':' ', '2A':' ', '3A':' ', '4A':' ', '5A':' ',
        '1B':' ', '2B':' ', '3B':' ', '4B':' ', '5B':' ',
        '1C':' ', '2C':' ', '3C':' ', '4C':' ', '5C':' ',
        '1D':' ', '2D':' ', '3D':' ', '4D':' ', '5D':' ',
        '1E':' ', '2E':' ', '3E':' ', '4E':' ', '5E':' ',
        }
    ships_locs = []
    print('Hey Player! Where do you wanna place your ships (enter 6 locations)')
    while len(ships_locs) < 6:
        loc = input()
        if loc not in board.keys():
            print('That\'s out of range!')
        if loc in ships_locs:
            print('The slot is occupied, dude!')
        else: 
            ships_locs.append(loc)
    for loc in ships_locs:
        board[loc] = 'O'
    return board
