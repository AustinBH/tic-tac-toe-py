import random
# Initial variables for players and game state
# Added win tracker
players = {
    'player1': {
        'name': 'Player 1',
        'team': '',
        'wins': 0
    },
    'player2': {
        'name': 'Player 2',
        'team': '',
        'wins': 0
    }
}
playing = True
# Creating empty board to hold 9 elements
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# Creating example board to display where choices go
example_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Creating initial player team selection and starting welcome message
def welcome():
    global players
    # Need to confirm that players select a valid team
    players['player1']['team'] = input('Select your team (X or O): ').upper()
    if players['player1']['team'] == 'X':
        players['player2']['team'] = 'O'
    elif players['player1']['team'] == 'O':
        players['player2']['team'] = 'X'
    else:
        print('That is not a correct team!')
        welcome()
# As board is using empty strings to start, we can just display the rows and columns
def display_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
# This function will allow the user to choose their move
def get_user_choice(player):
    global board
    global playing
    while True:
        choice = input(f"{player['name']} what is your move? (1-9)\n")
        # Adding exit to game and while loop
        if choice and choice[0].lower() == 'q':
            playing = False
            break
        # Adding error handling
        try:
            choice = int(choice)
        except ValueError:
            print("That's not a valid move!")
        else:
            # Preventing overwriting previous moves, want to check on all rows of board
            if board[choice -1] == ' ':
                board[choice -1] = player['team']
            else:
                print("That's not a valid move!")
                get_user_choice(player)
            check_win(player)
            display_board(board)
            break

def check_win(player):
    global board
    global players
    # cannot win diagonally at this time
    if player['team'] in board and (check_horizontal(board, player['team']) or check_vertical(board, player['team']) or check_diagonal(board, player['team'])):
        print(f"{player['name']} wins!")
        # This logic can be made dryer as well
        if player['name'] == 'Player 1':
            players['player1']['wins'] += 1
        else:
            players['player2']['wins'] += 1
        print(f"{player['name']} now has {player['wins']} wins!")
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# It works but needs to be dryed up this is very wet at the moment
def check_horizontal(board, player):
    if (board[0] == player and board[0] == board[1] and board[1] == board[2]) or (board[3] == player and board[3] == board[4] and board[4] == board[5]) or (board[6] == player and board[6] == board[7] and board[7] == board[8]):
        return True

def check_vertical(board, player):
    if (board[0] == player and board[0] == board[3] and board[3] == board[6]) or (board[1] == player and board[1] == board[4] and board[4] == board[7]) or (board[2] == player and board[2] == board[5] and board[5] == board[8]):
        return True

def check_diagonal(board, player):
    if (board[0] == player and board[0] == board[4] and board[4] == board[8]) or (board[2] == player and board[2] == board[4] and board[4] == board[6]):
        return True

print('Welcome to Tic Tac Toe!')
welcome()
print('Here is an example of the Tic Tac Toe Board:')
display_board(example_board)
# Need to redo this as it forces player 2 to play again when game is over
if random.randint(1,10) > 5:
    while playing:
        get_user_choice(players['player1'])
        get_user_choice(players['player2'])
else:
    while playing:
        get_user_choice(players['player2'])
        get_user_choice(players['player1'])

print(f"{players['player1']['name']} won {players['player1']['wins']} times!")
print(f"{players['player2']['name']} won {players['player2']['wins']} times!")
if players['player1']['wins'] > players['player2']['wins']:
    print('Player 1 Wins!')
else:
    print('Player 2 Wins!')
