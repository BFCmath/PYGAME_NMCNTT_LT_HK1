import numpy

dir_x = numpy.array((-1, -1, 0, 1))
dir_y = numpy.array((0, -1, -1, 1))

def inside(numRow, numCol, x, y):
    return (0 <= x <= numRow) and (0 <= y <= numCol)
    
def checkWin(numRow, numCol, cur_row, cur_col, cnt):
    ok = False
    for t in range(4):
        both = 1

        pre_x = cur_row + dir_x[t]
        pre_y = cur_col + dir_y[t]
        if inside(numRow, numCol, pre_x, pre_y):
            both += cnt[pre_x][pre_y] 
            cnt[cur_row][cur_col][t] = cnt[pre_x][pre_y][7 - t] + 1
        else:
            cnt[cur_row][cur_col][t] = 1

        nxt_x = cur_row - dir_x[t]
        nxt_y = cur_row - dir_y[t]
        if inside(numRow, numCol, pre_x, pre_y):
            both += cnt[nxt_x][nxt_y]
            cnt[cur_row][cur_col][7 - t] = cnt[nxt_x][nxt_y][t]  + 1
        else:
            cnt[cur_row][cur_col][7 - t] = 1

        ok |= both >= 5

    return ok
