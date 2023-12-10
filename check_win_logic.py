dir_x = (1, 0, -1, -1)
dir_y = (-1, -1, -1, 0)

def inside(num_row, num_col, cur_x, cur_y):
    return (0 <= cur_x < num_row) and (0 <= cur_y < num_col)

def blocked(num_row, num_col, exc_x, exc_y, cnt_p, turn):
    return inside(num_row, num_col, exc_x, exc_y) and cnt_p[exc_x][exc_y][0][turn] > 0

def check_win(num_row, num_col, cur_x, cur_y, cnt_p, turn, wins):
    for i in range(4):
        pre_x = cur_x + dir_x[i]
        pre_y = cur_y + dir_y[i]
        pre_len = 0
        if inside(num_row, num_col, pre_x, pre_y) and (cnt_p[pre_x][pre_y][i][turn] > 0):
            pre_len = cnt_p[pre_x][pre_y][i][turn]
            pre_x = cur_x + pre_len * dir_x[i]
            pre_y = cur_y + pre_len * dir_y[i]
        else:
            pre_x = cur_x
            pre_y = cur_y
        pre_blocked = blocked(num_row, num_col, pre_x + dir_x[i], pre_y + dir_y[i], cnt_p, 1 - turn)

        nxt_x = cur_x - dir_x[i]
        nxt_y = cur_y - dir_y[i]
        nxt_len = 0
        if inside(num_row, num_col, nxt_x, nxt_y) and (cnt_p[nxt_x][nxt_y][7 - i][turn] > 0):
            nxt_len = cnt_p[nxt_x][nxt_y][7 - i][turn]
            nxt_x = cur_x - nxt_len * dir_x[i]
            nxt_y = cur_y - nxt_len * dir_y[i]
        else:
            nxt_x = cur_x
            nxt_y = cur_y
        nxt_blocked = blocked(num_row, num_col, nxt_x - dir_x[i], nxt_y - dir_y[i], cnt_p, 1 - turn)
        
        cnt_p[pre_x][pre_y][7 - i][turn] = cnt_p[nxt_x][nxt_y][i][turn] = pre_len + 1 + nxt_len
        if (pre_len + nxt_len > 3) and ((pre_blocked & nxt_blocked) == False):
            wins.append([(pre_x, pre_y), (nxt_x, nxt_y)])