#################################
## Project: Sliding Puzzle     ##
## Copyright ReadyPython Sp19  ##
#################################
from copy import deepcopy
from random import choice
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
        action = choice(get_legal_actions(new_board))
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
def solve(board):
    '''Return a list of actions which, taken on BOARD, solves the puzzle by
    turning the board into the following form:
    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 |   |
    -------------
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
                # return ["right", "up", "left", "down"]
                return [state[1] for state in path][1:] # We only need to return a list of actions
            for action in get_legal_actions(last_board):
                new_state = [take(action, last_board), action]
                new_path = path + [new_state]
                q.append(new_path)
    return "NO_SOLUTION"

# from utils import PriorityQueue
# def solve(board):
#     visited = set() # This stores boards converted to strings from 2D lists.
#     pq = PriorityQueue()
#     pq.push([[board, None]], 0) # The elements on the fringe are (board_state, last_action). push(item, priority)
#     while not pq.isEmpty():
#         path = pq.pop()
#         last_board = path[-1][0]
#         if str(last_board) not in visited:
#             visited.add(str(last_board))
#             if is_goal(last_board):
#                 # return path
#                 # return ["right", "up", "left", "down"]
#                 return [state[1] for state in path][1:] # We only need to return a list of actions
#             for action in get_legal_actions(last_board):
#                 new_state = [take(action, last_board), action]
#                 new_path = path + [new_state]
#                 length_so_far = len(new_path)
#                 pq.push(new_path, length_so_far + idealMinumumSteps(board))
#     return "NO_SOLUTION"
#
# def heuristics(board):
#     ''' Returns the total number of misplaced numbers in BOARD.
#     Note that this heuristics is admissible and consistent.'''
#     count = 0
#     for row in range(len(board)):
#         for col in range(len(board[0])):
#             if board[row][col] != row * 3 + col + 1:
#                 count += 1
#     return count
