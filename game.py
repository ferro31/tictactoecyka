import copy
import os
import random

import generatepossiblemoves

board = [['X', 'X', 'X'],
         ['X', 'X', 'X'],
         ['X', 'X', 'X']]


def format_board(b):
    a = ''
    for row in b:
        for b in row:
            a += str(b)
    return a


def format_board_to_num(b):
    a = []
    for row in b:
        for field in row:
            a.append(field)
    return a


def format_board_to_matrix(board):
    return [board[:3], board[3:6], board[6:]]


def print_board_pretty(board):
    for row in board[::3]:
        print(row)


def check_orientation(board, original):
    if board == original: return True
    board_copy = format_board(board)
    rotated_board = ["", "", "", "", "", "", "", "", ""]
    rotations = [(0, 2), (3, 1), (6, 0), (1, 5), (4, 4), (7, 3), (2, 8), (5, 7), (8, 6)]
    for i in range(3):
        for rotation in rotations:
            rotated_board[rotation[1]] = int(board_copy[rotation[0]])
        if format_board_to_matrix(rotated_board) == original:
            return True
        board_copy = copy.deepcopy(rotated_board)
    return False


def check_saved():
    if os.path.exists(f"moves/{format_board(board)}.txt"):
        with open(f"moves/{format_board(board)}.txt", 'r') as f:
            return f.readline().split(",")
    else:
        with open(f"moves/{format_board(board)}.txt", 'w+') as f:
            f.write(",".join(list(generatepossiblemoves.generate_possibilies(board))))
            return list(generatepossiblemoves.generate_possibilies(board))


def remove(chosen, possibilties, boardcopy):
    possible_moves = copy.deepcopy(possibilties)
    possible_moves.remove(chosen)
    with open(f"moves/{format_board(boardcopy)}.txt", 'w') as f:
        f.write(",".join(possible_moves))


def simulate_one_game(board):
    which = "P"
    is_going = True
    while is_going:
        try:
            make_computer_move(which)
            which = "P" if which == "C" else "C"
        except Exception as e:
            print("kys", e)
            is_going = False


def make_computer_move(which):
    global board
    board_temp = copy.deepcopy(board)
    possibilities = check_saved()
    c = random.choice(possibilities)
    board[int(c[0])][int(c[1])] = which
    return False


def make_computer_move_and_await(which):
    global board
    board_temp = copy.deepcopy(board)
    possibilities = check_saved()
    c = random.choice(possibilities)
    board[int(c[0])][int(c[1])] = which
    if int(input()):
        remove(c, possibilities, boardcopy)
        board = copy.deepcopy(board_temp)
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        for a in board:
            print(a)
        # p = input()
        # board[int(p[0])][int(p[1])] = "P"
        boardcopy = copy.deepcopy(board)
        # while make_computer_move_and_await("P"):
        #     print("ni")

        # while make_computer_move_and_await("C"):
        #     print("ni")
        simulate_one_game(boardcopy)
        for a in board:
            print(a)

        print("*---*")
