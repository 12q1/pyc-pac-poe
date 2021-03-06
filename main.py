#################################################################
# Simple tic-tac-toe style game using python
# No external resources used except looking up some methods
#################################################################

#################################################################
# Imports
#################################################################

import os

#################################################################
# Function Declarations
#################################################################


def display_board(current_board):
    os.system('cls' if os.name == 'nt' else 'clear')
    # clears terminal
    '''
    Takes an array of length 9 and prints an ascii grid representing a tic-tac-toe board
    **Only prints to CLI or some stdOut does not return anything**
    Example input: [_,_,_,_,x,_,_,_,_]
    Example output: _|_|_
                    _|x|_
                    _|_|_
    '''
    print(f'   {current_board[6]}|{current_board[7]}|{current_board[8]}')
    print(f'   {current_board[3]}|{current_board[4]}|{current_board[5]}')
    print(f'   {current_board[0]}|{current_board[1]}|{current_board[2]}')
    # Reverse board because I use board index directly in take_turn() so this format is more efficient


def take_turn(board, xo):
    '''
    Takes two parameters - a board array and a boolean representing x or o as True or False
    Example expected input : [_,_,_,_,_,_,_,_,_] , True
    Example expected output : [_,_,x,_,_,_,_,_,_]
    '''
    if xo == True:
        letter = 'x'
    else:
        letter = 'o'
    position = int(input(
        f"{letter}'s turn: where do you want to place your mark? (Hint: use your numpad) "))
    board[position-1] = letter
    return board
    # TODO prevent player from putting their mark on an existing position


def check_win_condition(board):
    '''
    Takes an array of 9 length and checks whether there are any 3-in-a-row states vertically, horizontally or diagonally
    if one of these states is true then the game is won and a bool True is returned
    else it returns False
    '''
    def check_horizontals(board):
        temp_string = "".join(board[:3]) + "|" + "".join(board[3:6]) + "|" + "".join(board[6:])
        return 'xxx' in temp_string or 'ooo' in temp_string


    def check_verticals(board):
        temp_string = "".join([board[6], board[3], board[0]]) + '|' + "".join([board[7], board[4], board[1]]) + "|" + "".join([board[8], board[5], board[2]])
        return 'xxx' in temp_string or 'ooo' in temp_string


    def check_diagonals(board):
        temp_string = "".join([board[6], board[4], board[2]]) + "|" + "".join([board[8], board[4], board[0]])
        return 'xxx' in temp_string or 'ooo' in temp_string
        
    return check_diagonals(board) or check_horizontals(board) or check_verticals(board)


def start_game():
    '''
    Initiates a new game by resetting the board and player and continues until game_over condition is met
    once a game is over the loop is terminated and the function prompts the user if they want to replay
    if replay is chosen the function calls itself semi-recursively
    else it calls a hard exit 
    '''
    print('Starting game...')
    board = ['_'] * 9
    display_board(board)
    player = True
    game_over = False
    while game_over == False:
        board = take_turn(board, player)
        display_board(board)
        player = not player
        game_over = check_win_condition(board)
        if game_over:
            if player == True:
                letter = 'O'
            else:
                letter = 'X'
            restart = input(f'{letter} won! would you like to replay the game? y/n : ').lower()
            if restart == 'y':
                start_game()
            else:
                print('Alright have a nice day!')
                exit()


#################################################################
# Game Initialization Logic
#################################################################


run_game = input('Do you want to start a game of pyc-pac-poe? y/n : ').lower()

if run_game == 'y':
    start_game()
else:
    print('Alright have a nice day!')
    exit()

# EOF
