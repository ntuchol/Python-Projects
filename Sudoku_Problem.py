def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True  # Puzzle solved
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack

    return False

def is_valid(board, num, pos):
    # Check row, column, and 3x3 box for validity
    pass # Implementation details here

def find_empty(board):
    # Find and return the coordinates of an empty cell (0)
    pass # Implementation details here

# Example usage:
# board = [[...], [...], ...]  # Your Sudoku puzzle
# if solve_sudoku(board):
#     print("Solved Sudoku:")
#     # Print the solved board
# else:
#     print("No solution exists.")