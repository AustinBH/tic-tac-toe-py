import random

player = ''
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
    global player
    print('Welcome to Tic Tac Toe!')
    player = input('Select your team (X or O): ').upper()
# As board is using empty strings to start, we can just display the rows and columns
def display_board(board):
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
    print('-----------')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
    print('-----------')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')
# This function will allow the user to choose their move
def get_user_choice():
    global board
    global player
    choice = int(input('What is your move?\n'))
    # Need to add handling for if a user inputs a string that cannot be converted to int
    if choice >= 1 and choice <= 3:
        board[0][choice - 1] = player
    elif choice >= 4 and choice <= 6:
        board[1][choice%3 - 1] = player
    elif choice >= 7 and choice <= 9:
        board[2][choice%3 - 1] = player
    else:
        print('Choose a valid move')
        get_user_choice()
    display_board(board)
    
welcome()
print('Here is an example of the Tic Tac Toe Board:')
display_board(example_board)
get_user_choice()
