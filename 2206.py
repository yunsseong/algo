from collections import deque
import sys, copy

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, list(input()))))

w_maze = copy.deepcopy(maze)

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

cnt = 0
move = 1

start_row, start_col = 0, 0
end_row, end_col = n-1, m-1

q = deque()
q.append((start_row, start_col, 0))
q_len = len(q)

maze[0][0] = 1
w_maze[0][0] = 1

while len(q) > 0:
    r, c, w = q.pop()

    if r == end_row and c == end_col:
        print(move)
        sys.exit()

    cnt += 1

    for i in range(len(dr)):
        nr = dr[i] + r
        nc = dc[i] + c

        if 0 <= nr < n and 0 <= nc < m:
            if w == 0:
                if maze[nr][nc] == 0:
                    maze[nr][nc] = 1
                    q.appendleft((nr, nc, w))
                else:
                    w_maze[nr][nc] = 1
                    q.appendleft((nr, nc, 1))
            else:
                if w_maze[nr][nc] == 0:
                    w_maze[nr][nc] = 1
                    q.appendleft((nr, nc, w))

    if len(q) == 0:
        print(-1)
        sys.exit()

    if q_len == cnt:
        move += 1
        cnt = 0
        q_len = len(q)
