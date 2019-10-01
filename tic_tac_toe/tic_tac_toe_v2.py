import random
from termcolor import colored
#Adding players, both user and computer
players = [
    {
        'name': 'User',
        'team': '',
        'wins': 0
    },
    {
        'name': 'Computer',
        'team': '',
        'wins': 0
    }
]
playing = True
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# Creating example board to display where choices go
example_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Creating initial player team selection and starting welcome message

def welcome():
    global players
    # Need to confirm that the player selects a valid team
    players[0]['team'] = colored(
        input('Select your team (X or O): ').upper(), 'green')
    if players[0]['team'] == colored('X', 'green'):
        players[1]['team'] = colored('0', 'cyan')
    elif players[0]['team'] == colored('O', 'green'):
        players[1]['team'] = colored('X', 'cyan')
    else:
        print('That is not a correct team!')
        welcome()


def display_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


def get_user_choice(player):
    global board
    global playing
    while True:
        choice = input("Player1 what is your move? (1-9)\n")
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
            # Preventing overwriting previous moves, want to check on all rows
            # of board
            if board[choice - 1] == ' ':
                board[choice - 1] = player['team']
            else:
                print("That's not a valid move!")
                get_user_choice(player)
            check_win(player)
            display_board(board)
            break
    
def get_computer_choice(player):
    global board
    global playing
    while True:
        # This is currently just a random choice and the computer does not block the user
        choice = random.randint(1, 9)
        if board[choice-1] == ' ':
            board[choice -1] = player['team']
        else:
            get_computer_choice(player)
        check_win(player)
        display_board(board)
        break


def check_win(player):
    global board
    global players
    # cannot win diagonally at this time
    if player['team'] in board and (
        check_horizontal(
            board,
            player['team']) or check_vertical(
            board,
            player['team']) or check_diagonal(
                board,
            player['team'])):
        print(f"{player['name']} wins!")
        # This logic can be made dryer as well
        if player['name'] == 'User':
            players[0]['wins'] += 1
        else:
            players[1]['wins'] += 1
        print(f"{player['name']} now has {player['wins']} wins!")
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def check_horizontal(board, player):
    if (
        board[0] == player and board[0] == board[1] and board[1] == board[2]) or (
        board[3] == player and board[3] == board[4] and board[4] == board[5]) or (
            board[6] == player and board[6] == board[7] and board[7] == board[8]):
        return True


def check_vertical(board, player):
    if (
        board[0] == player and board[0] == board[3] and board[3] == board[6]) or (
        board[1] == player and board[1] == board[4] and board[4] == board[7]) or (
            board[2] == player and board[2] == board[5] and board[5] == board[8]):
        return True


def check_diagonal(board, player):
    if (board[0] == player and board[0] == board[4] and board[4] == board[8]) or (
            board[2] == player and board[2] == board[4] and board[4] == board[6]):
        return True
# Starting game, picking teams and displaying example board
print('Welcome to Tic Tac Toe!')
welcome()
print('Here is an example of the Tic Tac Toe Board:')
display_board(example_board)

if random.randint(1, 10) > 5:
    while playing:
        get_user_choice(players[0])
        get_computer_choice(players[1])
else:
    while playing:
        get_computer_choice(players[1])
        get_user_choice(players[0])

print(f"{players[0]['name']} won {players[0]['wins']} times!")
print(f"{players[1]['name']} won {players[1]['wins']} times!")
if players[0]['wins'] > players[1]['wins']:
    print('User wins!')
else:
    print('Computer wins :( try again later...')
