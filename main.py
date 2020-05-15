# Simple tic-tac-toe style game using python
# No external resources used except looking up some methods

def display_board(current_board):
    print(f'{current_board[6]}|{current_board[7]}|{current_board[8]}')
    print(f'{current_board[3]}|{current_board[4]}|{current_board[5]}')
    print(f'{current_board[0]}|{current_board[1]}|{current_board[2]}')

def take_turn(board, xo):
    if(xo == True):
        letter = 'x'
    else:
        letter = 'o'
    position = int(input(f"{letter}'s turn: where do you want to place your mark? (hint: use your numpad) "))
    board[position-1] = letter
    return board

def check_win_condition():
    pass

def start_game():
    print('Starting game...')
    board = ['_'] * 9
    display_board(board)
    player = True
    game_over = False
    while game_over == False:
        board = take_turn(board, player)
        display_board(board)
        player = not player


run_game = input('Do you want to start a game of pyc-pac-poe? y/n : ').lower()

if run_game == 'y':
    start_game()
else:
    print('Alright have a nice day!')
    exit()

#EOF