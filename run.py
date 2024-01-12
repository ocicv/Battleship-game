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

## How to dispay boards
def display_board(board):
    print('----------------------')
    print('| ' + board['1A'] + ' | ' + board['2A'] + ' | ' + board['3A'] + ' | ' + board['4A'] + ' | ' + board['5A'] + ' |')
    print('----------------------')
    print('| ' + board['1B'] + ' | ' + board['2B'] + ' | ' + board['3B'] + ' | ' + board['4B'] + ' | ' + board['5B'] + ' |')
    print('----------------------')
    print('| ' + board['1C'] + ' | ' + board['2C'] + ' | ' + board['3C'] + ' | ' + board['4C'] + ' | ' + board['5C'] + ' |')
    print('----------------------')
    print('| ' + board['1D'] + ' | ' + board['2D'] + ' | ' + board['3D'] + ' | ' + board['4D'] + ' | ' + board['5D'] + ' |')
    print('----------------------')
    print('| ' + board['1E'] + ' | ' + board['2E'] + ' | ' + board['3E'] + ' | ' + board['4E'] + ' | ' + board['5E'] + ' |')
    print('----------------------')
    

## function to play Battleship
def game():
    ## create boards for NPC and player
    pc_board = create_board_computer()
    player_board = create_board_player()
    
    ## display player's board
    display_board(player_board)
    
    ## variables to control when the game ends
    turn = 'Player'
    pc_point = 6
    player_point = 6
    round = 0
    
    ## lists to keep track of player and NPC's moves
    pc_moves = []
    player_moves = []
    
    for i in range(25):
        if turn == 'Player':
            print('----------------------')
            print('\033[1mPlayer turn:\033[0m')
            move = input()
            if move not in player_board.keys():
                print('You hit a homerun! It\'s just not a good thing in this game.')
            elif move in player_moves:
                print('C\'mon! You hit it twice! That is cheating.')
            else: 
                if pc_board[move] == 'O':
                    pc_point -= 1 
                    print(f'Nice shot, Player. {pc_point} to go!')
                else:
                    print('Oh! That was a miss. Try harder next time.')
            
            player_moves.append(move)
        
        if turn == 'Computer':
            print('----------------------')
            print('\033[1mComputer turn:\033[0m')
            move = random.sample(player_board.keys(), 1)
            print(move[0])
            if player_board[move[0]] == 'O':
                player_point -= 1
                print(f'Nice shot, Computer. {player_point} to go!')
            elif move in pc_moves:
                print('C\'mon! You hit it twice! That is cheating.')
            else:
                print('Oh! That was a miss. Try harder next time.')

            pc_moves.append(move)
            