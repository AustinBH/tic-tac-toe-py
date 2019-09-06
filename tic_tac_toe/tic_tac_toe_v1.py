import random

player = ''
# Creating empty board to hold 3 rows
board = [
    ['X', 'O'],
    [],
    []
]
# Creating initial player team selection and starting welcome message
def welcome():
    global player
    print('Welcome to Tic Tac Toe!')
    player = input('Select your team (X or O): ').upper()
# Helper method for our board method to return 
def display_index(row, col):
    global board
    # Need to figure out the correct logic to make sure that we dont throw error
    # Still W.I.P
    if board[row] and board[row][col]:
        return board[row][col]
    return ''

def display_board():
    print(f' {display_index(0,0)} | {display_index(0,1)} | {display_index(0,2)} ')
    print(f' {display_index(1,0)} | {display_index(1,1)} | {display_index(1,2)} ')
    print(f' {display_index(2,0)} | {display_index(2,1)} | {display_index(2,2)} ')



display_board()
