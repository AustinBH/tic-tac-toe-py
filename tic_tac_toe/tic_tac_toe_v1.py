# Initial variables for players and game state
players = {
    'player1': '',
    'player2': ''
}
playing = True
# Creating empty board to hold 3 rows
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
# Creating example board to display where choices go
example_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Creating initial player team selection and starting welcome message
def welcome():
    global players
    print('Welcome to Tic Tac Toe!')
    players['player1'] = input('Select your team (X or O): ').upper()
    if players['player1'] == 'X':
        players['player2'] = 'O'
    else:
        players['player2'] = 'X'
# As board is using empty strings to start, we can just display the rows and columns
def display_board(board):
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
    print('-----------')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
    print('-----------')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')
# This function will allow the user to choose their move
def get_user_choice(player):
    global board
    choice = int(input(f'{player} what is your move?\n'))
    # Need to add handling for if a user inputs a string that cannot be converted to int
    if choice >= 1 and choice <= 3:
        board[0][choice - 1] = player
    elif choice >= 4 and choice <= 6:
        board[1][choice%3 - 1] = player
    elif choice >= 7 and choice <= 9:
        board[2][choice%3 - 1] = player
    else:
        print('Choose a valid move')
        get_user_choice(player)
    check_win(player)
    display_board(board)

def check_win(player):
    global board
    global playing
    # current version only checks horizontal + vertical, no diagonal check
    if board[0][0] == player and (board[0][0] == board[1][0] and board[1][0] == board[2][0]) or (board[0][0] == board[0][1] and board[0][1] == board[0][2]):
        print(f'{player} wins!')
        playing = False

    
welcome()
print('Here is an example of the Tic Tac Toe Board:')
display_board(example_board)
while playing:
    get_user_choice(players['player1'])
    get_user_choice(players['player2'])
