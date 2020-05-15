#################################################################
# Simple tic-tac-toe style game using python
# No external resources used except looking up some methods
#################################################################


#################################################################
# Function Declarations
#################################################################

def display_board(current_board):
    '''
    Takes an array of length 9 and prints an ascii grid representing a tic-tac-toe board
    **Only prints to CLI or some stdOut does not return anything**
    Example input: [_,_,_,_,x,_,_,_,_]
    Example output: _|_|_
                    _|x|_
                    _|_|_
    '''
    print(f'{current_board[6]}|{current_board[7]}|{current_board[8]}')
    print(f'{current_board[3]}|{current_board[4]}|{current_board[5]}')
    print(f'{current_board[0]}|{current_board[1]}|{current_board[2]}')
    # Reverse board because I use board index directly in take_turn () so this format is more efficient


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
    #TODO prevent player from putting their mark on an existing position


def check_win_condition(board):
    '''
    Takes an array of 9 length and checks whether there are any 3-in-a-row states vertically, horizontally or diagonally
    if one of these states is true then the game is won and a bool True is returned
    else it returns False
    '''
    #TODO there's probably a better way to check win conditions than bruteforcing it like this
    if len(set([board[0], board[1], board[2]])) == 1 or len(set([board[3], board[4], board[5]])) == 1 or len(set([board[6], board[7], board[8]])) == 1:
        # Check horizontals
        return True
    elif len(set([board[6], board[3], board[0]])) == 1 or len(set([board[7], board[4], board[1]])) == 1 or len(set([board[8], board[5], board[2]])) == 1:
        # Check verticals
        return True
    elif len(set([board[6], board[4], board[2]])) == 1 or len(set([board[8], board[4], board[0]])) == 1:
        # Check diagonals
        return True
    else:
        return False


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
            print('Game Over')


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
