def check_win(turn, row, col,matrix,row_cell,col_cell):
    count = 0
    block = 0
    r = max(row - 1, 0)
    while (r > -1 and matrix[r][col] == turn):
        count = count + 1
        r = r - 1
    if r == -1 or matrix[r][col] == -turn:
        block = block + 1
    r = min(row + 1 , row_cell)
    while ( r < row_cell and matrix[r][col] == turn):
        count = count + 1
        r = r + 1
    if r == row_cell or matrix[r][col] == -turn:
        block = block + 1
    if (count > 3 and block < 2):
        return True

    count = 0
    block = 0
    c = max(col - 1, 0)
    while (c > -1 and matrix[row][c] == turn):
        count = count + 1
        c = c - 1
    if c == -1 or matrix[row][c] == -turn:
        block = block + 1
    c = min(col + 1 , col_cell)
    while (c < col_cell and matrix[row][c] == turn):
        count = count + 1
        c = c + 1
    if c == col_cell or matrix[row][c] == -turn:
        block = block + 1
    if (count > 3 and block < 2):
        return True

    count = 0
    block = 0
    i = 1
    while ( row + i < row_cell and col + i < col_cell and matrix[row + i][col + i] == turn ):
        count = count + 1
        i = i + 1
    if row + i == row_cell or col + i == col_cell or matrix[row + i][col + i] == -turn:
        block = block + 1
    i = 1
    while (row - i > -1 and col - i > -1 and matrix[row - i][col - i] == turn):
        count = count + 1
        i = i + 1
    if row - i == -1 or col - i == col_cell or matrix[row - i][col - i] == -turn:
        block = block + 1
    if (count > 3 and block < 2):
        return True    

    count = 0
    block = 0
    i = 1
    while (row + i < row_cell and col - i > -1 and matrix[row + i][col - i] == turn  ):
        count = count + 1
        i = i + 1
    if row + i == row_cell or col - i == col_cell or matrix[row + i][col - i] == -turn:
        block = block + 1
    i = 1
    while (row - i > -1 and col + i < col_cell and matrix[row - i][col + i] == turn ):
        count = count + 1
        i = i + 1
    if row - i == -1 or col + i == col_cell or matrix[row - i][col + i] == -turn:
        block = block + 1
    if (count > 3 and block < 2):
        return True 

    return False