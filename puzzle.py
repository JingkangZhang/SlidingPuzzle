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
REVERSE_ACTION_MAP = {"up": "down", "down": "up", "left": "right", "right": "left"}
INSTR_MAP = {
    "right": "right",
    "r": "right",
    "left": "left",
    "l": "left",
    "up": "up",
    "u": "up",
    "down": "down",
    "d": "down",
    "reset": "reset",
    "quit": "quit",
    "solve": "solve"
    }

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
    print("-------------")
    for row in range(len(board)):
        print("| ", end="")
        for col in range(len(board[0])):
            content = board[row][col]
            print(content if content != 0 else " ", end=" | ")
        print("\n-------------")

def play():
    ''' Plays a sliding puzzle game by
    1. Shuffle the sample_board to get the initial board state
    2. Ask the user whether to show the generated solution animation
        if yes:
            1. Solve the puzzle and obtain a list of actions
            2. Visualize the solution
    3. Enter the game loop: ask the user for actions and update boards until solved
    '''
    board = shuffle(sample_board)
    print("This is the randomly shuffled initial state:")
    print_board(board)
    show_solution = input("Would you like to see the solution animation? (yes/no): ")
    while show_solution not in ("yes", "no"):
        show_solution = input("Please input yes/no: ")
    if show_solution == "yes":
        print("Solving...")
        actions = solve(board)
        if actions == "NO_SOLUTION": # A correct shuffle function should NOT result in NO_SOLUTION.
            print("There is no solution from current state.")
            return
        print("Solved!")
        input("Press Enter to start visualization: ")
        visualize(board, actions)
    else:
        ori_board = deepcopy(board)
        num_actions = 0
        instruction = input("u)p, d)own, r)ight, l)eft, reset, or quit: ")
        display_board = True
        while True:
            if display_board:
                cls()
                print_board(board)
            else:
                display_board = True
            if is_goal(board):
                print("Puzzle solved! Steps taken:", num_actions)
                return

            while instruction not in INSTR_MAP:
                instruction = input("u)p, d)own, r)ight, l)eft, reset, or quit: ")

            instruction = INSTR_MAP[instruction]

            if instruction == "reset":
                board = deepcopy(ori_board)
                num_actions = 0
            elif instruction == "quit":
                print("Quitting...")
                return
            elif instruction == "solve":
                print("Solution is: ", solve(board))
                display_board = False
            else:
                num_actions += 1
                instruction = REVERSE_ACTION_MAP[instruction]
                if instruction not in get_legal_actions(board):
                    print("Illegal action:", REVERSE_ACTION_MAP[instruction])
                    display_board = False
                else:
                    board = take(instruction, board)
            instruction = None



def visualize(board, actions):
    ''' Visualize the transitions in BOARD by printing each states after taking actions.
    Transition time interval: 1 second. The screen is cleared by calling cls() before printing. '''
    copy = deepcopy(board)
    cls()
    print_board(copy)
    sleep(1)
    for action in actions:
        copy = take(action, copy)
        cls()
        print_board(copy)
        sleep(1)
    print("Solved! Total steps:", len(actions))
    print("Initial state:")
    print_board(board)
    print("Actions took:", actions, "(Actions are defined as ways the empty slot is moved around.)")

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
    pass #FIXME

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
    zero_pos = find_zero(board)
    board_rows = len(board)
    board_cols = len(board[0])
    actions = ACTIONS[:]
    if _: #FIXME
        actions.remove("up")
    if _: #FIXME
        actions.remove("down")
    if _: #FIXME
        actions.remove("left")
    if _: #FIXME
        actions.remove("right")
    return actions

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
    zero_pos = find_zero(board)
    zero_row = zero_pos[0]
    zero_col = zero_pos[1]
    new_board = deepcopy(board)
    if action == "up":
        pass #FIXME
    if action == "down":
        pass #FIXME
    if action == "left":
        pass #FIXME
    if action == "right":
        pass #FIXME
    return new_board

def shuffle(board):
    '''Return a new board obtained by taking 50 random
    actions from BOARD. '''
    new_board = deepcopy(board)
    for i in range(50):
        action = choice(get_legal_actions(new_board))
        new_board = take(action, new_board)
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
    visited = set() # This stores boards converted to strings from 2D lists.
    q = []
    q.append([[board, None]]) # The elements on the fringe are (board_state, last_action)
    while q:
        path = q.pop(0)
        last_board = path[-1][0]
        if str(last_board) not in visited:
            visited.add(str(last_board))
            if is_goal(last_board):
                # return path
                return [state[1] for state in path][1:] # We only need to return a list of actions
            for action in get_legal_actions(last_board):
                new_state = [take(action, last_board), action]
                new_path = path + [new_state]
                q.append(new_path)
    return "NO_SOLUTION"

def cls():
    '''Clears the terminal screen.'''
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == '__main__':
    print("====================================================")
    print("Welcome to ReadyPython Project: Silding Puzzle!")
    play()
