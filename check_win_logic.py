<<<<<<< HEAD
import numpy

dir_x = numpy.array((-1, -1, 0, 1))
dir_y = numpy.array((0, -1, -1, -1))

num_row = 9
num_col = 9
cnt_p = numpy.zeros([num_row, num_col, 8, 2])

def inside(num_row, num_col, cur_x, cur_y):
    return (0 <= cur_x <= num_row) and (0 <= cur_y <= num_col)

def check_win(num_row, num_col, cur_x, cur_y, cnt_p, turn):
    is_win = False
    for i in range(4):
        pre_x = cur_x + dir_x[i]
        pre_y = cur_y + dir_y[i]
        pre_len = cnt_p[pre_x][pre_y][i][turn]
        if inside(num_row, num_col, pre_x, pre_y) and (pre_len > 0):
            pre_x = cur_x + pre_len * dir_x[i]
            pre_y = cur_y + pre_len * dir_y[i]
        else:
            pre_x = cur_x
            pre_y = cur_y
            pre_len = 0

        nxt_x = cur_x - dir_x[i]
        nxt_y = cur_y - dir_y[i]
        nxt_len = cnt_p[nxt_x][nxt_y][7 - i][turn]
        if inside(num_row, num_col, nxt_x, nxt_y) and (nxt_len > 0):
            nxt_x = cur_x - nxt_len * dir_x[i]
            nxt_y = cur_y - nxt_len * dir_y[i]
        else:
            nxt_x = cur_x
            nxt_y = cur_y
            nxt_len = 0
        
        total = pre_len + 1 + nxt_len
        cnt_p[pre_x][pre_y][7 - i][turn] = cnt_p[nxt_x][nxt_y][i][turn] = total
        is_win |= total >= 5

    return is_win
=======
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
>>>>>>> d4d626426466491d11ad2da2957abbae167de1c7
