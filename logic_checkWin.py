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