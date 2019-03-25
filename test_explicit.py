from puzzle import solve
import time
import random
import sys
from copy import deepcopy

sample_board = [ #represented as a 2D list
    [1,2,3],
    [4,5,6],
    [7,8,0] # 0 stands for the empty slot
]
ACTIONS = ["up", "down", "left", "right"] #Actions are represented as ways to move the empty slot (0) around.


def print_board(board):
    '''Print BOARD to console in the following format:
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

def find_zero(board):
    '''Return the coordinate as (row_number, column_number)
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
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return row, col

def get_legal_actions(board):
    '''Return a list of legal actions in BOARD. Actions are represented
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
    if zero_pos[0] == 0:
        actions.remove("up")
    if zero_pos[0] == board_rows - 1:
        actions.remove("down")
    if zero_pos[1] == 0:
        actions.remove("left")
    if zero_pos[1] == board_cols - 1:
        actions.remove("right")
    return actions

def take(action, board):
    '''Return the resulting board after taking ACTION on BOARD,
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
        new_board[zero_row][zero_col], new_board[zero_row - 1][zero_col] = new_board[zero_row - 1][zero_col], new_board[zero_row][zero_col]
    if action == "down":
        new_board[zero_row][zero_col], new_board[zero_row + 1][zero_col] = new_board[zero_row + 1][zero_col], new_board[zero_row][zero_col]
    if action == "left":
        new_board[zero_row][zero_col], new_board[zero_row][zero_col - 1] = new_board[zero_row][zero_col - 1], new_board[zero_row][zero_col]
    if action == "right":
        new_board[zero_row][zero_col], new_board[zero_row][zero_col + 1] = new_board[zero_row][zero_col + 1], new_board[zero_row][zero_col]
    return new_board

def shuffle(board):
    '''Return a new board obtained by taking 50 random
    actions from BOARD. '''
    new_board = deepcopy(board)
    for i in range(50):
        action = random.choice(get_legal_actions(new_board))
        new_board = take(action, new_board)
    return new_board

def is_goal(board):
    '''Return True iff BOARD is
    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 |   |
    -------------'''
    return board == [[1,2,3],[4,5,6],[7,8,0]]

def test(seed=None):
    '''Run solve() 50 times on randomly shuffled 3x3 boards,
    check for correctness and record total elapsed time.'''
    print("==============================================")
    print("Running 50 randomized tests:\n")
    random.seed(a=seed)
    total_time = 0
    passed = 0
    for i in range(50):
        if i % 10 == 0:
            print("Running test", i + 1, "-", i + 10, "...")
        board = shuffle(sample_board)
        start = time.time()
        solution = solve(board[:])
        # print("Solution is", solution)
        end = time.time()
        total_time += end - start
        if not check(solution, board, passed):
            print("Current test terminated.")
            print("==============================================")
            return
        passed += 1
    print("All tests passed. solve() total running time:", total_time, "s")
    print("==============================================")

def check(solution, board, passed):
    transitions = [[board,None]]
    # actions = []
    for i in range(len(solution)):
        action = solution[i]
        if action not in get_legal_actions(transitions[-1][0]):
            print("{} tests passed before encountering the first failed case.".format(passed))
            print_transitions(transitions)
            print("Illegal action:", action.__repr__())
            # print_board(transitions[-1])
            return False
        # actions.append(action)
        next_state = take(action, transitions[-1][0])
        # print("......")
        # print_board(next_state)
        transitions.append([next_state, action])
        # print("*******")
        # print(transitions)
    if not is_goal(transitions[-1][0]):
        print("{} tests passed before encountering the first failed case.".format(passed))
        print_transitions(transitions)
        print("The above state is not the goal state.")
        return False
    return True

def print_transitions(trans):
    print("Initial state:")
    print_board(trans[0][0])
    trans.pop(0)
    for state, action in trans:
        print("Taking action:", action)
        print_board(state)

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
test(seed)
