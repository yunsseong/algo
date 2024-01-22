from collections import deque
import sys

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, list(input()))))

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

cnt = 0
move = 0

start_row, start_col = 0, 0
end_row, end_col = n-1, m-1

q = deque()
q.append((start_row, start_col))
q_len = len(q)

while len(q) > 0:
    r, c = q.pop()

    if r == end_row and c == end_col:
        print(move+1)
        sys.exit()

    cnt += 1

    for i in range(len(dr)):
        nr = dr[i] + r
        nc = dc[i] + c

        if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == 1:
            maze[nr][nc] = 0
            q.appendleft((nr, nc))

    if q_len == cnt:
        move += 1
        cnt = 0
        q_len = len(q)

