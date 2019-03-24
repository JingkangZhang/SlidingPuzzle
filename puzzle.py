from copy import deepcopy
from random import choice
sample_board = [
    [4,1,3],
    [2,8,0],
    [7,6,5]
]
ACTIONS = ["up", "down", "left", "right"]
def print_board(board):
    print("-------------")
    for row in range(len(board)):
        print("| ", end="")
        for col in range(len(board[0])):
            content = board[row][col]
            print(content if content != 0 else " ", end=" | ")
        print("\n-------------")

def shuffle(board):
    new_board = deepcopy(board)
    for i in range(50):
        action = choice(get_legal_actions(new_board))
        new_board = take(action, new_board)
    return new_board

def find_zero(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return row, col

def take(action, board):
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
    
def get_legal_actions(board):
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
