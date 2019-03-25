#################################
## Project: Sliding Puzzle     ##
## Copyright ReadyPython Sp19  ##
## All rights reserved.        ##
#################################

from copy import deepcopy # Used to copy boards represented as 2D lists
from random import choice # Used in shuffle() to choose randomly from legal actions
from time import sleep # Used in visualization
import os # useful for clear console screen utility

sample_board = [ #represented as a 2D list
    [1,2,3],
    [4,5,6],
    [7,8,0] # 0 stands for the empty slot
]
ACTIONS = ["up", "down", "left", "right"] #Actions are represented as ways to move the empty slot (0) around.

def print_board(board):
    '''Prints BOARD to console in the following format:
    -------------
    | 4 | 3 | 6 |
    -------------
    |   | 5 | 7 |
    -------------
    | 1 | 8 | 4 |
    -------------
    '''
    "*** YOUR CODE HERE ***"

def play():
    ''' Plays a sliding puzzle game by
    1. Shuffling the sample_board to get initial board state
    2. Solve the puzzle and obtain a list of actions
    3. Visualize the solution
    '''
    board = shuffle(sample_board)
    print("This is the randomly shuffled initial state:")
    print_board(board)
    print("Solving...")
    actions = solve(board)
    if actions == "NO_SOLUTION": # A correct shuffle function should NOT result in NO_SOLUTION.
        print("There is no solution from current state.")
        return
    print("Solved!")
    input("Press Enter to start visualization: ")
    visualize(board, actions)

def visualize(board, actions):
    ''' Visualize the transitions in BOARD by printing each states after taking actions.
    Transition time interval: 1 second. The screen is cleared by calling cls() before printing. '''
    "*** YOUR CODE HERE ***"

def find_zero(board):
    '''Returns the coordinate as (row_number, column_number)
    of "0" (the empty slot) in BOARD.

    E.g.
    The zero coordinate of the following board is (1, 0)
    -------------
    | 2 | 3 | 6 |
    -------------
    |   | 5 | 7 |
    -------------
    | 1 | 8 | 4 |
    -------------
    '''
    "*** YOUR CODE HERE ***"

def get_legal_actions(board):
    '''Returns a list of legal actions in BOARD. Actions are represented
    as ways to move the empty slot (0) around. An action should be in
    ["up", "down", "left", "right"].

    E.g. In the following board, the legal actions are ["up", "down", "right"].
    -------------
    | 2 | 3 | 6 |
    -------------
    |   | 5 | 7 |
    -------------
    | 1 | 8 | 4 |
    -------------'''
    "*** YOUR CODE HERE ***"

def take(action, board):
    '''Returns the resulting board after taking ACTION on BOARD,
    assuming ACTION is legal. ACTION should be in ["up", "down", "left", "right"].
    Actions are represented as ways to move the empty slot (0) around.

    E.g.
    -------------
    | 2 | 3 | 6 |
    -------------
    |   | 5 | 7 |
    -------------
    | 1 | 8 | 4 |
    -------------
    Taking action "up" in the above board will result in the following board:
    -------------
    |   | 3 | 6 |
    -------------
    | 2 | 5 | 7 |
    -------------
    | 1 | 8 | 4 |
    -------------
    '''
    assert action in ACTIONS, "Invalid action: '{}'".format(action)
    "*** YOUR CODE HERE ***"

def shuffle(board):
    '''Return a new board obtained by taking 50 random
    actions from BOARD. '''
    new_board = deepcopy(board)
    for i in range(50):
        #FIXME
    return new_board

def is_goal(board):
    '''Returns True iff BOARD is
    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 |   |
    -------------'''
    return board == [[1,2,3],[4,5,6],[7,8,0]]

def solve(board):
    '''Returns a list of actions which, taken on BOARD, solves the puzzle by
    turning the board into the following form:
    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 |   |
    -------------
    Returns "NO_SOLUTION" if there is no solution.
    '''
    "*** YOUR CODE HERE ***"

def cls():
    '''Clears the terminal screen.'''
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == '__main__':
    print("====================================================")
    print("Welcome to ReadyPython Project: Silding Puzzle!")
    play()
