from game import check_orientation
from minimax import generate_scores

b1 = [[1, 2, 1],
      [2, 2, 0],
      [2, 0, 2]]

b2 = [[1, 1, 2],
      [2, 0, 0],
      [0, 0, 0]]

# print(check_orientation(b1, b2))  # Expected output: True if b2 is the transpose of b1
print(generate_scores(b2, 3, 0, 0))







