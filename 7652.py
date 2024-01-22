from collections import deque

times = int(input())

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [-1, -2, -2, -1, 1, 2, 2, 1]


for _ in range(times):
    cnt = 0
    move = 0
    board_len = int(input())
    start_row, start_col = map(int, input().split())
    end_row, end_col = map(int, input().split())

    chess_map = [[0 for _ in range(board_len)] for _ in range(board_len)]
    chess_map[start_row][start_row] = 1
    q = deque()
    q.append((start_row, start_col))
    q_len = len(q)

    while len(q) > 0:
        r, c = q.pop()
        cnt += 1

        if r == end_row and c == end_col:
            break

        for i in range(len(dr)):
            nr = dr[i] + r
            nc = dc[i] + c

            if 0 <= nr < board_len and 0 <= nc < board_len and chess_map[nr][nc] == 0:
                chess_map[nr][nc] = 1
                q.appendleft((nr, nc))

        if q_len == cnt:
            move += 1
            cnt = 0
            q_len = len(q)

    print(move)