from puzzle import *
import time
def test():
    '''Run solve() 50 times on randomly shuffled 3x3 boards,
    check for correctness and record total elapsed time.'''
    print("==============================================")
    print("Running 50 randomized tests:\n")
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
        print("Took action:", action)
        print_board(state)
