from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
t = int(input())

for _ in range(t):
    cnt = 0
    col_len, row_len, b_cnt = map(int, input().split())
    b_map = [[0 for _ in range(col_len)] for _ in range(row_len)]
    b_cord = deque()
    for _ in range(b_cnt):
        col, row = map(int, input().split())
        b_cord.append([row, col])
        b_map[row][col] = 1

    c_cord = deque()
    while b_cnt > 0:
        row, col = b_cord.pop()

        if b_map[row][col] == 1:
            b_cnt -= 1
            b_map[row][col] = 0
            c_cord.append([row, col])

            while len(c_cord) > 0:
                row, col = c_cord.pop()
                for i in range(4):
                    cord = [row + dr[i], col + dc[i]]
                    if 0 <= cord[0] < row_len and 0 <= cord[1] < col_len and b_map[cord[0]][cord[1]] == 1:
                        c_cord.append(cord)
                        b_map[cord[0]][cord[1]] = 0
                        b_cnt -= 1
            cnt += 1

    print(cnt)

