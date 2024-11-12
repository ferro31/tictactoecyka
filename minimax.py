import copy
import math
from generatepossiblemoves import generate_possibilies
import sys

sys.setrecursionlimit(2147483647)


def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # base case : targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))

    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))


def generate_scores(board, depth, current_depth, turn):
    # Base case: if max depth reached, evaluate the board
    if current_depth == depth:
        return evaluate_board(board)  # Define `evaluate_board` as needed

    turns = [1, 2]
    possibilities = generate_possibilies(board)  # Get all possible moves
    scores = []

    # Use backtracking instead of deepcopy for efficiency
    for possibility in possibilities:
        row, col = possibility
        board[row][col] = turns[turn % 2]  # Make the move

        # Recursive call to explore further moves
        score = generate_scores(board, depth, current_depth + 1, turn + 1)
        scores.append(score)

        # Undo the move (backtracking)
        board[row][col] = 0

    # Decide how to combine scores based on the turn
    return max(scores) if turn % 2 == 0 else min(scores)


def evaluate_board(board):
    total_value = 0
    winning_combinations = [
        # Rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    matching = []
    for move in [[1, -5, -10], [2, 5, 10]]:
        m = []
        for combination in winning_combinations:
            c = []
            for indexes in combination:
                c.append(board[indexes[0]][indexes[1]] == move[0])
            m.append(c)

        matching.append(m)
        matching.append("")
    b = 1
    for comb in matching:
        if comb == "":
            b *= -1
            continue
        for a in comb:
            for c in a:
                if c:
                    total_value += 5 * b
    return total_value


scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 3)

print("The optimal value is : ", end="")
print(minimax(0, 0, True, scores, treeDepth))
