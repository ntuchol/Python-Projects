def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True  
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  

    return False

def is_valid(board, num, pos):
    pass 

def find_empty(board):
    pass 

