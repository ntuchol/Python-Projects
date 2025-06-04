ddef find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, num, pos):
    for i in range(9):
        if board[pos[0]][i] == num or board[i][pos[1]] == num:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def solve_sudoku(board):
    find = find_empty_location(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

example_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(example_board):
    for row in example_board:
        print(row)
else:
    print("Solution doesn't exist")