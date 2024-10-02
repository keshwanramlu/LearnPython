#Global Variables
board = [' ' for x in range(0,9)]
moved = set()
winning_combo = ['012','048','036','147','246','258','345','678']
winner = False

#Initialise board
def initialize_board():
    for x in range(0,9):
        board[x] = ' '
    
#DisplayBoard
def print_board():
    print('printing board ...\n')
    if len(board) > 0:
        print('|'.join(board[0:3]))
        print('|'.join(board[3:6]))
        print('|'.join(board[6:9]))
        print('\n')
    else:
        print('Board has not been initialized!')
    
#GetUserInput
def get_user_input(user_char):
    invalid_move = True
    while invalid_move and len(moved) <= 9:
        move = input('Enter the position to move between 0-9: ')
        if move.isdigit():
            position = int(move)
            if position >= 0 and position < 9 and position not in moved:
                moved.add(position)
                board[position] = user_char
                invalid_move = False
            else:
                print('Invalid move!')
            
#CheckWin
def check_win(user_char):
    print('Checking winner ...')
    for i in winning_combo:
        if user_char == board[int(i[0])] and user_char == board[int(i[1])] and user_char == board[int(i[2])]:
            global winner 
            winner = True
            return winner
        else:
            pass
    return False
            
    
#Play Game
def play_game():
    keep_playing = True
    global winner
    print_board()
    users = ['','']
    users[0] = input('User 1 enter name: ')
    users[1] = input('User 2 enter name: ')
    print('Tic Tac Toe challenge between ' + users[0] + ' and ' + users[1])
    next_move = ['X','O']
    while len(moved) <= 9 and not winner:
        user = len(moved)%2
        get_user_input(next_move[user])
        print_board()
        if check_win(next_move[user]):
            print(users[user] + ' has won!')
        if len(moved) == 9 or winner:
            keep_playing = input('Do you want to play another game? Enter Y or N: ')
            if keep_playing.lower() == 'y':
                initialize_board()
                moved.clear()
                winner = False
                print_board()
            else:
                break
 #Execute   
play_game()