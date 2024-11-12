import os
import copy


def generate_possibilies(board):
    for i, row in enumerate(board):
        for i2, place in enumerate(row):
            if place == 0:
                yield f"{i}{i2}"

# rounds = 1
#
# starting_board = [['X', 'X', 'X'],
#                   ['X', 'X', 'X'],
#                   ['X', 'X', 'X'],]
#
#
# def generate_boards(board):
#     for i, r in enumerate(board):
#         for i2, p in enumerate(row):
#             if p == "X":
#                 yield f"{i}{i2}"
#
# for i in range(rounds):
#     next_board = copy.deepcopy(starting_board)
#
#     if not os.path.exists(f"moves/round{i}"):
#         os.mkdir(f"moves/round{i}")
#
#     for ind, row in enumerate(next_board):
#         for ind2, place in enumerate(row):
#             if place == 'X':
#                 next_board[ind][ind2] = 'P'
#                 for coord in generate_boards(next_board):
#                     with open(f"moves/round{i}/possibility{ind * 3 + ind2}.txt", "w") as f:
#                         f.write(coord)
#                         print(coord)
#             next_board = copy.deepcopy(starting_board)
