import random

player = ''
# Creating empty board to hold 3 rows
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
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
    print('-----------')

welcome()
print('Here is an example of the Tic Tac Toe Board:')
display_board(example_board)
display_board(board)
